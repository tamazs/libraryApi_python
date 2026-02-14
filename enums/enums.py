from enum import Enum


class MembershipType(str, Enum):
    student = "student"
    faculty = "faculty"
    public = "public"