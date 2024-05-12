"""
Test custom Django management commands.

"""
#check db , wait and then again check db

# patch to mock behavior of db adn simulate response of db
from unittest.mock import patch

# possible error we might get,to connect db before db is ready
from psycopg2 import OperationalError as Psycopg20pError
# Cal cammadn by that we are testing, by the naem
from django.core.management import call_command
# exception we may get depending on stages of connection
from django.db.utils import OperationalError
#testing behavior that db is not available, so dont need migrations
# we are just simuation db so we use stcase
from django.test import SimpleTestCase 

#mock, we do it for all so we use decorator?
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db is ready"""
        #just return a value True from patched check 
        patched_check.return_value = True

    # test db is ready adn commadn is set up
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases = ['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self,patched_sleep,patched_check):
        """Test waiting for database when getting OperationalError."""
        #raise exception if db is not ready.Side effect
        # the first two tiems we call mock method wer raise PsychoError
        # next three times raise operation error from django
        # 6th time we get True as a value than exception
        patched_check.side_effect = [Psycopg20pError] * 2 + [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        # we only expect check command only 6 times rather than again and again
        # we make sure that it is callled 6 times
        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_with(databases = ['default'])