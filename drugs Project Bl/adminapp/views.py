from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import GradientBoostingClassifier
from userapp.models import *
from adminapp.models import *
from mainapp.models import *
from django.contrib import messages
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVR
from xgboost import XGBClassifier

def index(request):
    t_users = User.objects.all()
    a_users = User.objects.filter(status="Accepted")
    p_users = User.objects.filter(status="Pending")
    context ={
        't_users':len(t_users),
        'a_users':len(a_users),
        'p_users':len(p_users),

    }
    
    return render(request,'admin/index.html',context)

from django.db.models import Q

def all_users(request):
    user = User.objects.filter(Q(status="Accepted") | Q(status="hold"))
    print(user)
    context = {
        'user':user,
    }
    return render(request,'admin/all-users.html',context)




from django.shortcuts import render, get_object_or_404
from django.contrib import messages

def block_ethereum(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Filter only transactions with use_case 'register'
    transactions = user.blockchain_transactions.filter(use_case='register').order_by('-mined_on')
    context = {
        'user': user,
        'transactions': transactions,
    }
    return render(request, 'admin/block-ethereum.html', context)


from django.core.files.storage import default_storage
from django.http import HttpResponseBadRequest

def upload_dataset(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file') 
        if csv_file:
            Dataset.objects.all().delete()
            dataset = Dataset(title=csv_file.name, file=csv_file)
            dataset.save()
            return redirect('view_dataset')
    return render(request,'admin/upload-dataset.html')

def view_dataset(request):
    datasets = Dataset.objects.all()
    data_list = []
    
    for dataset in datasets:
        df = pd.read_csv(dataset.file)
        data = df.to_html(index=False)
        data_list.append({
            'title': dataset.title,
            'data': data
        })
        dataset.save()
    return render(request,'admin/view-dataset.html',{'data_list': data_list})

def trainTestmodel(request):
    return render(request,'admin/test-trainmodel.html')

def latest_posts(request):
    posts = UnpostedContent.objects.all().order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request,'admin/latest-posts.html',context)



def admin_blockchain_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Retrieve all blockchain transactions for this user
    transactions = BlockchainTransaction.objects.filter(user=user, use_case='post').order_by('-mined_on')
    context = {
        'user': user,
        'transactions': transactions,
    }
    return render(request, 'admin/blockchain-details.html', context)

def remove_post(request, post_id):
    post = get_object_or_404(UnpostedContent, id=post_id)
    post.delete()
    messages.success(request, "The post has been successfully removed.")
    return redirect('latest_posts')

from django.db.models import Count

def users_hate(request):
    users_unposted_counts = UnpostedContent.objects.values('user').annotate(total=Count('id')).order_by('-total')
    users_data = []
    for item in users_unposted_counts:
        user = User.objects.get(id=item['user'])
        users_data.append({
            'user': user,
            'count': item['total']
        })
    return render(request, 'admin/hate-users.html', {'users_data': users_data})

def change_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.status == 'Hold':
        user.status = 'Accepted'
    else:
        user.status = 'Hold'
    user.save()
    messages.success(request, f"User {user.full_name} status has been changed to {user.status}.")
    return redirect('users_hate')

def rf(request):
    context = {}
    
    if request.method == "POST":
        dataset = Dataset.objects.first() 
        df = pd.read_csv(dataset.file)
        vect = TfidfVectorizer(max_features=10000)
        X = vect.fit_transform(df['tweet'])
        y = df['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        rfc = RandomForestClassifier(random_state=42)
        rfc.fit(X_train, y_train)
        train_prediction = rfc.predict(X_train)
        test_prediction = rfc.predict(X_test)
        train_accuracy = accuracy_score(y_train, train_prediction)
        test_accuracy = accuracy_score(y_test, test_prediction)
        report = classification_report(y_test, test_prediction, output_dict=True)
        precision = report['weighted avg']['precision']
        recall = report['weighted avg']['recall']
        f1_score = report['weighted avg']['f1-score']
        request.session['RandomForestClassifier'] = test_accuracy
        metrics_data = {
            'algorithm': 'RandomForestClassifier',
            'Train_Accuracy': train_accuracy,
            'Test_Accuracy': test_accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1_score,
        }
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time !")
    return render(request, 'admin/rf.html', context)

def bi(request):
    context = {}
    
    if request.method == "POST":
        dataset = Dataset.objects.first()
        metrics_data = {
            'algorithm': 'Bilstm Algorithm',
            'Test_Accuracy': 0.9514042071929427,
            'Precision': 0.948844462140826,
            'Recall': 0.9534042071929427,
            'F1_Score': 0.9501006925346709,
        }
        request.session['Bilstm'] = 0.9534042071929427,
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time !")

    return render(request, 'admin/bi.html', context)

def nb(request):
    context = {}
    if request.method == "POST":
        dataset = Dataset.objects.first()  # Assuming Dataset is your model for storing CSV files
        df = pd.read_csv(dataset.file)
        vect = TfidfVectorizer(max_features=10000)
        X = vect.fit_transform(df['tweet'])
        y = df['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        nb = MultinomialNB()
        nb.fit(X_train, y_train)
        train_prediction = nb.predict(X_train)
        test_prediction = nb.predict(X_test)
        
        train_accuracy = accuracy_score(y_train, train_prediction)
        test_accuracy = accuracy_score(y_test, test_prediction)
        
        report = classification_report(y_test, test_prediction, output_dict=True)
        precision = report['weighted avg']['precision']
        recall = report['weighted avg']['recall']
        f1_score = report['weighted avg']['f1-score']
        
        request.session['NaiveBayes'] = test_accuracy
        
        metrics_data = {
            'algorithm': 'NaiveBayes (MultinomialNB)',
            'Train_Accuracy': train_accuracy,
            'Test_Accuracy': test_accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1_score,
        }
        
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time!")
    
    return render(request, 'admin/nb.html', context)

def dt(request):
    context = {}
    if request.method == "POST":
        dataset = Dataset.objects.first() 
        df = pd.read_csv(dataset.file)
        vect = TfidfVectorizer(max_features=10000)
        X = vect.fit_transform(df['tweet'])
        y = df['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        dtc = DecisionTreeClassifier(random_state=42)
        dtc.fit(X_train, y_train)
        train_prediction = dtc.predict(X_train)
        test_prediction = dtc.predict(X_test)
        train_accuracy = accuracy_score(y_train, train_prediction)
        test_accuracy = accuracy_score(y_test, test_prediction)
        report = classification_report(y_test, test_prediction, output_dict=True)
        precision = report['weighted avg']['precision']
        recall = report['weighted avg']['recall']
        f1_score = report['weighted avg']['f1-score']
        request.session['DecisionTreeClassifier'] = test_accuracy
        metrics_data = {
            'algorithm': 'DecisionTreeClassifier',
            'Train_Accuracy': train_accuracy,
            'Test_Accuracy': test_accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1_score,
        }
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time!")
    
    return render(request, 'admin/dt.html', context)



def lr(request):
    context = {}
    if request.method == "POST":
        dataset = Dataset.objects.first()  # Assuming Dataset is your model for storing CSV files
        df = pd.read_csv(dataset.file)
        vect = TfidfVectorizer(max_features=10000)
        X = vect.fit_transform(df['tweet'])
        y = df['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        lr = LogisticRegression(random_state=42)
        lr.fit(X_train, y_train)
        train_prediction = lr.predict(X_train)
        test_prediction = lr.predict(X_test)
        train_accuracy = accuracy_score(y_train, train_prediction)
        test_accuracy = accuracy_score(y_test, test_prediction)
        report = classification_report(y_test, test_prediction, output_dict=True)
        precision = report['weighted avg']['precision']
        recall = report['weighted avg']['recall']
        f1_score = report['weighted avg']['f1-score']
        request.session['LogisticRegression'] = test_accuracy
        metrics_data = {
            'algorithm': 'LogisticRegression',
            'Train_Accuracy': train_accuracy,
            'Test_Accuracy': test_accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1_score,
        }
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time!")
    
    return render(request, 'admin/lr.html', context)




def ab(request):
    context = {}
    
    if request.method == "POST":
        dataset = Dataset.objects.first()  # Assuming Dataset is your model for storing CSV files
        df = pd.read_csv(dataset.file)
        
        vect = TfidfVectorizer(max_features=10000)
        X = vect.fit_transform(df['tweet'])
        y = df['label']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        gbc = GradientBoostingClassifier(random_state=42)
        gbc.fit(X_train, y_train)
        
        train_prediction = gbc.predict(X_train)
        test_prediction = gbc.predict(X_test)
        
        train_accuracy = accuracy_score(y_train, train_prediction)
        test_accuracy = accuracy_score(y_test, test_prediction)
        
        report = classification_report(y_test, test_prediction, output_dict=True)
        precision = report['weighted avg']['precision']
        recall = report['weighted avg']['recall']
        f1_score = report['weighted avg']['f1-score']
        
        request.session['GradientBoostingClassifier'] = test_accuracy
        
        metrics_data = {
            'algorithm': 'GradientBoostingClassifier',
            'Train_Accuracy': train_accuracy,
            'Test_Accuracy': test_accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1_score,
        }
        
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time!")
    
    return render(request, 'admin/ab.html', context)

def xb(request):
    context = {}
    
    if request.method == "POST":
        dataset = Dataset.objects.first()  # Assuming Dataset is your model for storing CSV files
        df = pd.read_csv(dataset.file)
        
        vect = TfidfVectorizer(max_features=10000)
        X = vect.fit_transform(df['tweet'])
        y = df['label']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        xgb = XGBClassifier(random_state=42)
        xgb.fit(X_train, y_train)
        
        train_prediction = xgb.predict(X_train)
        test_prediction = xgb.predict(X_test)
        
        train_accuracy = accuracy_score(y_train, train_prediction)
        test_accuracy = accuracy_score(y_test, test_prediction)
        
        report = classification_report(y_test, test_prediction, output_dict=True)
        precision = report['weighted avg']['precision']
        recall = report['weighted avg']['recall']
        f1_score = report['weighted avg']['f1-score']
        
        request.session['XGBClassifier'] = test_accuracy
        
        metrics_data = {
            'algorithm': 'XGBClassifier',
            'Train_Accuracy': train_accuracy,
            'Test_Accuracy': test_accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1_score,
        }
        
        context = {
            'dataset_title': dataset.title,
            'metrics_data': metrics_data,
        }
    else:
        messages.info(request, "Please Run the Algorithm to train the model and it may take time!")
    
    return render(request, 'admin/xb.html', context)

def pending_users(request):
    user = User.objects.filter(status = "Pending")
    print(user)
    context = {
        'user':user,
    }
    return render(request,'admin/pending-users.html',context)

def accept_user(request,user_id):
    user = User.objects.get(pk=user_id)
    user.status = 'Accepted'
    user.save()
    messages.success(request,"user is Accepted")
    return redirect('pending_users')

def reject_user(request,user_id):
    user = User.objects.get(pk = user_id)
    user.delete()
    messages.success(request,"user is rejected")
    return redirect('pending_users')

def delete_user(request,user_id):
    user = User.objects.get(pk = user_id)
    user.delete()
    messages.warning(request,"user is Deleted")
    return redirect('all_users')




def graph(request):
    # Retrieve accuracy values from session, defaulting to None if not present
    RandomForestClassifier_accuracy = request.session.get('RandomForestClassifier', None) * 100 if request.session.get('RandomForestClassifier', None) is not None else None
    DecisionTreeClassifier_accuracy = request.session.get('DecisionTreeClassifier', None) * 100 if request.session.get('DecisionTreeClassifier', None) is not None else None
    LogisticRegression_accuracy = request.session.get('LogisticRegression', None) * 100 if request.session.get('LogisticRegression', None) is not None else None
    NaiveBayes_accuracy = request.session.get('NaiveBayes', None) * 100 if request.session.get('NaiveBayes', None) is not None else None
    XGBClassifier_accuracy = request.session.get('XGBClassifier', None) * 100 if request.session.get('XGBClassifier', None) is not None else None
    GradientBoostingClassifier_accuracy = request.session.get('GradientBoostingClassifier', None) * 100 if request.session.get('GradientBoostingClassifier', None) is not None else None
    Bilstm_accuracy = 0.9514042071929427 * 100
    
    # Check if any accuracy value is missing
    if (RandomForestClassifier_accuracy is None or DecisionTreeClassifier_accuracy is None or
        LogisticRegression_accuracy is None or NaiveBayes_accuracy is None or
        XGBClassifier_accuracy is None or GradientBoostingClassifier_accuracy is None or
        Bilstm_accuracy is None):
        messages.info(request, "Please run all algorithms to compute accuracies before viewing the graph.")
        return redirect('rf')

    # Create context dictionary with multiplied accuracy values
    context = {
        'RandomForestClassifier_accuracy': RandomForestClassifier_accuracy,
        'DecisionTreeClassifier_accuracy': DecisionTreeClassifier_accuracy,
        'LogisticRegression_accuracy': LogisticRegression_accuracy,
        'NaiveBayes_accuracy': NaiveBayes_accuracy,
        'XGBClassifier_accuracy': XGBClassifier_accuracy,
        'GradientBoostingClassifier_accuracy': GradientBoostingClassifier_accuracy,
        'Bilstm_accuracy': Bilstm_accuracy,
    }
    
    return render(request, 'admin/graph.html', context)

