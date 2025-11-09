// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    // Declare variables
    address public owner;
    uint256 private balance;

    // Constructor: set contract deployer as owner
    constructor() {
        owner = msg.sender;
        balance = 0;
    }

    // Modifier to allow only owner to perform certain actions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Function to deposit money into the account
    function deposit() public payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balance += msg.value;
    }

    // Function to withdraw money
    function withdraw(uint256 amount) public onlyOwner {
        require(amount <= balance, "Insufficient balance");
        balance -= amount;
        payable(owner).transfer(amount);
    }

    // Function to view current balance
    function showBalance() public view returns (uint256) {
        return balance;
    }
}
