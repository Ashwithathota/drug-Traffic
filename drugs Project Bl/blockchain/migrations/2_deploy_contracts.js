// migrations/2_deploy_contracts.js
const Cannatch = artifacts.require("Cannatch");

module.exports = function(deployer) {
  deployer.deploy(Cannatch, { gas: 4500000 });
};
