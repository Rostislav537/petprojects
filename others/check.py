from enchant.checker import SpellChecker

checker = SpellChecker()
checker.set_text("превет друк, как ты")
print([i.word for i in checker])