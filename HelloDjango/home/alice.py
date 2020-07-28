from alice_scripts import Skill, request, say, suggest

skill = Skill(__name__)


@skill.script
def run_script():
    yield say('Добрый день! Как вас зовут?')
    name = request.command


run_script()
print('ok', run_script())