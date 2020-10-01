"""
Example 1:
Input:
INSERT 'a'
INSERT 'b'

Output: "ab"

Example 2:
Input:
INSERT 'a'
INSERT 'b'
UNDO

Output: "a"

Example 3:
Input:
INSERT 'a'
INSERT 'b'
UNDO
REDO

Output: "ab"

Example 4:
Input:
INSERT 'a'
INSERT 'b'
UNDO
REDO
REDO # Does nothing

Output: "ab"


INSERT: Inserts a single character to the end of the string
DELETE: Removes the last character in the string
UNDO: Reverses the most recent action
REDO: Redoes the most recent action undone
"""


class Action:
    INSERT = "INSERT"
    DELETE = "DELETE"
    UNDO = "UNDO"
    REDO = "REDO"


def get_opposite_action(action: str) -> str:
    if action == Action.DELETE:
        return Action.INSERT

    return Action.DELETE


class TextEditor:
    def __init__(self, instructions: list) -> None:
        self.output = ""
        self.actions_taken = []
        self.all_removed = (
            ""  # track all that have been added, for multiple undo of delete
        )

        self.instructions = instructions
        self.item_to_add = None

    def insert_or_delete(self, action: Action) -> None:
        if action == Action.INSERT:
            if not self.all_removed:
                return
            self.insert_item(self.all_removed[-1])

        else:
            self.delete_item()

    def insert_item(self, item_to_add) -> None:
        self.output += item_to_add
        self.item_to_add = ""

    def delete_item(self) -> None:
        if not self.output:
            return

        self.all_removed += self.output[-1]
        self.output = self.output[:-1]

    def edit(self) -> str:
        for instruction in self.instructions:
            split_instr = instruction.split(" ")
            action = split_instr[0].replace("'", "")
            self.item_to_add = (
                split_instr[1].replace("'", "") if len(split_instr) > 1 else None
            )

            last_action = self.actions_taken[-1] if self.actions_taken else None
            self.actions_taken.append(action)

            if action == Action.INSERT:
                self.insert_item(self.item_to_add)
                self.all_removed = ""

            elif action == Action.DELETE:
                self.all_removed = ""
                self.delete_item()

            elif action == Action.UNDO:
                if not last_action:  # there is nothing to undo
                    self.actions_taken.pop()  # dont need to remember this action

                new_action = get_opposite_action(last_action)
                if new_action == Action.INSERT:
                    if not self.all_removed:  # nothing had been deleted to re-insert
                        continue

                self.insert_or_delete(new_action)

            elif action == Action.REDO:
                if last_action != Action.UNDO:
                    self.actions_taken.pop()  # dont need to remember this action
                    continue
                action_to_redo = self.actions_taken[
                    -3
                ]  # order will be [action, undo, redo]
                self.insert_or_delete(action_to_redo)

        return self.output


text_editor = TextEditor(["INSERT 'a'", "INSERT 'b'"])
assert text_editor.edit() == "ab"

text_editor1 = TextEditor(["INSERT 'a'", "INSERT 'b'", "UNDO"])
assert text_editor1.edit() == "a"

text_editor2 = TextEditor(["INSERT 'a'", "INSERT 'b'", "UNDO", "REDO"])
assert text_editor2.edit() == "ab"

text_editor3 = TextEditor(
    ["INSERT 'a'", "INSERT 'b'", "UNDO", "REDO", "REDO", "INSERT 'a"]
)
assert text_editor3.edit() == "aba"
