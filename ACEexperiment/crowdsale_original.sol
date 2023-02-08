pragma solidity >=0.4.24 <0.6.0;
contract Crowdsale {
    uint raised;
    uint goal;
    uint deadline;

    constructor(uint _goal) public {
        goal = _goal;
        deadline = now + 365 days;
    }

    function invest() public payable {
        require(now <= deadline);
        raised += msg.value;
    }

    function finish() public {
        require(address(this).balance >= goal);
    }

    function cancel() public {
        require(address(this).balance < goal && now > deadline);
    }
}
