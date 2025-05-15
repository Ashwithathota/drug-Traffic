// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Cannatch {
    // Event to log transaction details
    event TransactionExecuted(
        uint256 blockNumber,
        uint256 gasUsed,
        uint256 gasLimit,
        uint256 minedOn,
        bytes32 blockHash,
        address indexed fromAddress,
        address indexed toAddress,
        bytes32 txHash
    );

    // Function to simulate a blockchain transaction
    // Accepts a recipient address and a gas limit parameter.
    function executeTransaction(address to, uint256 _gasLimit) public returns (bool) {
        emit TransactionExecuted(
            block.number,
            gasleft(),
            _gasLimit,
            block.timestamp,
            blockhash(block.number - 1),
            msg.sender,
            to,
            keccak256(abi.encodePacked(block.timestamp, msg.sender, to))
        );
        return true;
    }
}
