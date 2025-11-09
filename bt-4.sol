// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure for Student details
    struct Student {
        uint256 id;
        string name;
        uint8 age;
        string course;
    }

    // Array to store multiple students
    Student[] public students;

    // Function to add student details
    function addStudent(uint256 _id, string memory _name, uint8 _age, string memory _course) public {
        students.push(Student(_id, _name, _age, _course));
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    // Function to get details of a specific student
    function getStudent(uint256 index) public view returns (uint256, string memory, uint8, string memory) {
        require(index < students.length, "Invalid student index");
        Student memory s = students[index];
        return (s.id, s.name, s.age, s.course);
    }

    // Fallback function — called when no matching function is found
    fallback() external payable {
        // Accept Ether and log that fallback was triggered
    }

    // Receive function — called when contract receives plain Ether
    receive() external payable {}
}
