// SPDX-License-Identifier: MIT
pragma solidity ^0.5.12;

contract Deposit {

    struct Payment {
        uint value; // сумма
        uint timestamp; // время
    }

    struct Member {
        Payment[] payments; // пополнения
        address referer; // реферер
        uint withdrawn; // сколько уже вывел процентов
        uint deposit; // сколько всего пополнил
        bool active;
    }

    mapping(address => Member) private members;
    address private owner;
    constructor() public {
        owner = msg.sender;
    }
    modifier isOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    // Function to receive Ether. msg.data must be empty
    function() external payable {
        if (msg.value == 0.0001 ether) {
            require(members[msg.sender].active, 'You are not have deposit');
            uint endDate = block.timestamp;
            uint reward = 0;

            for (uint i = 0; i < members[msg.sender].payments.length; i++) {
                uint diff = (endDate - members[msg.sender].payments[i].timestamp);

                if (diff >= 4) {  //40
                    reward += (members[msg.sender].payments[i].value * 2 / 100) * diff;
                }
            }

            uint amount = reward - members[msg.sender].withdrawn;
            address payable _to = address(uint160(msg.sender));
            _to.transfer(amount);
            members[msg.sender].withdrawn += amount;
        } else {
            require(msg.value > 0.1 ether, 'Minimum 0.1 ETH');
            if (!members[msg.sender].active && msg.data.length == 20) {
                address referer = bytesToAddress(bytes(msg.data));
                if (members[referer].active) {
                    members[msg.sender].referer = referer;
                    uint amount = msg.value * 20 / 100;
                    address payable _to = address(uint160(referer));
                    _to.transfer(amount);
                }
            }
            deposit(msg.sender, msg.value);
        }
    }

    function deposit(address sender, uint value) private {
        members[sender].active = true;
        members[sender].withdrawn = 0;
        members[sender].deposit += value;
        members[sender].payments.push(Payment(value, block.timestamp));
    }

    function bytesToAddress(bytes memory bys) private pure returns (address addr) {
        assembly {
            addr := mload(add(bys,20))
        }
    }

    function changeOwner(address newOwner) public isOwner {
        owner = newOwner;
    }

    function getMember(address _member) public view returns (address, uint, uint, bool) {
        return (members[_member].referer, members[_member].withdrawn, members[_member].deposit, members[_member].active);
    }

    function getPayments(address _member, uint indexOfPayment) public view returns (uint, uint) {
        return (members[_member].payments[indexOfPayment].value, members[_member].payments[indexOfPayment].timestamp);
    }

     function getWithdrawn(address _member) public view returns (uint) {
          return members[_member].withdrawn;
     }


    function getBalance() public view isOwner returns (uint256) {
        require(owner == msg.sender);
        return address(this).balance/(1 ether);
    }

    function withdraw(uint amount) public isOwner {
        amount = amount * (1 ether);
        require(address(this).balance >= amount);
        address payable _to = address(uint160(owner));
        _to.transfer(amount);
    }
}