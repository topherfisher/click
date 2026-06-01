import pytest 
from click.testing import CliRunner
from cli_tools.calculator import add_many

def test_add_many():
    runner = CliRunner()
    result = runner.invoke(add_many, ['10', '20'])
    assert result.exit_code == 0
    assert result.output == '30\n'

def test_add_many_verbose():
    runner = CliRunner()
    result = runner.invoke(add_many, ['10', '20', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 = 30\n'

def test_add_many_multiple():
    runner = CliRunner()
    result = runner.invoke(add_many, ['10', '20', '30', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 + 30 = 60\n'

    
# to run: in CLI -> pytest tests