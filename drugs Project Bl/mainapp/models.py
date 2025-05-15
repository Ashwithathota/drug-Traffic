from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="User Name")
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Password")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    age = models.CharField(max_length=15, verbose_name="Age")
    address = models.TextField(verbose_name="Address")
    photo = models.ImageField(upload_to='profiles/', verbose_name="Upload Profile", null=True, blank=True)
    otp = models.CharField(max_length=6, default='000000', help_text='Enter OTP for verification')
    otp_status = models.CharField(max_length=15, default='Not Verified', help_text='OTP status')
    status = models.CharField(max_length=15, default='Pending')

    INTEREST_CHOICES = [
        ('Reading', 'Reading'),
        ('Writing', 'Writing'),
        ('Drawing', 'Drawing'),
        ('Singing', 'Singing'),
        ('Dancing', 'Dancing'),
        ('Cooking', 'Cooking'),
        ('Gardening', 'Gardening'),
        ('Photography', 'Photography'),
        ('Sports', 'Sports'),
        ('Yoga', 'Yoga'),
        ('Meditation', 'Meditation'),
        ('Playing Musical Instruments', 'Playing Musical Instruments'),
        ('Watching Movies', 'Watching Movies'),
        ('Traveling', 'Traveling'),
        ('Volunteering', 'Volunteering'),
        ('Learning Languages', 'Learning Languages'),
        ('Coding', 'Coding'),
        ('Fashion', 'Fashion'),
        ('Painting', 'Painting'),
        ('Sculpting', 'Sculpting'),
        ('Collecting', 'Collecting'),
        ('Reading Comics', 'Reading Comics'),
    ]

    interests = models.ManyToManyField(
        'Interest',
        related_name='users',
        verbose_name="Interests",
        blank=True,
    )

    def __str__(self):
        return self.full_name

class Interest(models.Model):
    name = models.CharField(max_length=50, choices=User.INTEREST_CHOICES)

    def __str__(self):
        return self.name
    


class BlockchainTransaction(models.Model):
    USE_CASE_CHOICES = (
        ('register', 'Register'),
        ('post', 'Post'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blockchain_transactions', null=True, blank=True)
    block_no = models.CharField(max_length=100)
    gas_used = models.CharField(max_length=100)
    gas_limit = models.CharField(max_length=100)
    mined_on = models.DateTimeField()
    block_hash = models.CharField(max_length=100)
    from_address = models.CharField(max_length=100)
    to_address = models.CharField(max_length=100)
    tx_hash = models.CharField(max_length=100)
    use_case = models.CharField(max_length=20, choices=USE_CASE_CHOICES, default='register')
    
    def __str__(self):
        return f"Tx {self.tx_hash} for {self.user} ({self.use_case})"

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Friend request from {self.from_user.full_name} to {self.to_user.full_name}"