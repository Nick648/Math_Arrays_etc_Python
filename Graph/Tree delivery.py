class Tree:
    main_town = None

    def __init__(self, name: int, parent=None):
        self.name = name
        self.kids = []
        self.parent = parent
        self.product = 0
        if not parent:
            Tree.main_town = self

    def set_kids(self, kid):
        self.kids.append(kid)

    def get_name(self) -> int:
        return self.name

    def get_kids(self) -> list:
        return self.kids

    def get_parent(self):
        return self.parent

    def get_product(self) -> int:
        return self.product

    def delivery(self, level, package) -> None:
        self.product += package
        if level > 0:
            level -= 1
            for kid in self.get_kids():
                kid.delivery(level, package)

    def display_town(self, indent: str) -> None:
        print(f"{indent}{self.get_name()}")
        indent += "\t"
        for kid in self.get_kids():
            kid.display_town(indent)

    @classmethod
    def display_tree(cls) -> None:
        cur_town = Tree.main_town
        print(f"{cur_town.get_name()}")
        for kid in cur_town.get_kids():
            kid.display_town("\t")


def main() -> None:
    count_town = int(input())
    tree_town = [i + 1 for i in range(count_town)]
    tree_town[0] = Tree(1)
    for _ in range(count_town - 1):
        t_1, t_2 = map(int, input().split())
        if isinstance(tree_town[t_1 - 1], Tree):
            tree_town[t_2 - 1] = Tree(t_2, tree_town[t_1 - 1])
            tree_town[t_1 - 1].set_kids(tree_town[t_2 - 1])
        elif isinstance(tree_town[t_2 - 1], Tree):
            tree_town[t_1 - 1] = Tree(t_1, tree_town[t_2 - 1])
            tree_town[t_2 - 1].set_kids(tree_town[t_1 - 1])
    # print(f"{tree=}")
    # Tree.display_tree()
    transportation = int(input())
    for _ in range(transportation):
        num_town, level, package = map(int, input().split())
        tree_town[num_town - 1].delivery(level, package)

    for town in tree_town:
        if isinstance(town, Tree):
            print(f"{town.get_product()}", end=" ")
    print()


if __name__ == '__main__':
    main()
