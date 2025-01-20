class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def get_printable_info(self):
        return f'{self.name} ({self.designation})'

class TreeNode:
    def __init__(self, employee: Employee, parent = None):
        self.data = employee
        self.children = []
        self.parent = parent

    def get_level(self) -> int:
        level = 0
        current = self

        while current.parent is not None:
            level += 1
            current = current.parent

        return level

    def add_child(self, node):
        node.parent = self
        self.children.append(node)
    
    def get_prefix(self, level):
        return "|__" if level != 0 else ""
    
    def get_seperator(self, level):
        return level * "  "
    
    def print(self, allowed_level):
        level = self.get_level()

        if level > allowed_level:
            return
        
        print(
            self.get_seperator(level), 
            self.get_prefix(level), 
            self.data.get_printable_info(),
        )

        for child in self.children:
            child.print(allowed_level)

if __name__ == "__main__":
    ceo = TreeNode(Employee("Nilpul", "CEO"))
    cto = TreeNode(Employee("Chinmay", "CTO"))
    infra_head = TreeNode(Employee("Vishwa", "Infrastructure head"))
    cloud_manager = TreeNode(Employee("Dhaval", "Cloud manager"))
    app_manager = TreeNode(Employee("Abhijit", "App manager"))
    application_head = TreeNode(Employee("Aamir", "Application head"))
    hr_lead = TreeNode(Employee("Gels", "HR lead"))
    recruitment_manager = TreeNode(Employee("Peter", "Recruitment manager"))
    policy_manager = TreeNode(Employee("Waqas", "Policy manager"))

    ceo.add_child(cto)
    ceo.add_child(hr_lead)
    cto.add_child(infra_head)
    cto.add_child(application_head)
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)
    hr_lead.add_child(recruitment_manager)
    hr_lead.add_child(policy_manager)

    ceo.print(allowed_level=1)



