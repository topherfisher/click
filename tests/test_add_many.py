import pytest 
from click.testing import CliRunner
from cli_tools.calculator import add_many

def test_add_many():
    runner = CliRunner()
    result = runner.invoke(add_many, ['10', '20'])
    assert result.exit_code == 0
    assert result.output == '30\n'

# to run: in CLI -> pytest tests