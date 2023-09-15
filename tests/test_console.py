"""testing suite for the console"""

import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec, patch


class test_console(unittest.TestCase):
    """Testing the console module"""
    def setUp(self):
        """setup for"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        sys.stdout = self.backup

    def create(self):
        """creating an instance of the HBNBCommand class"""
        return HBNBCommand()

    def test_quit(self):
        """Testing quit exists"""
        console = self.create()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """Testing EOF exists"""
        console = self.create()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        """Test all exists"""
        console = self.create()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("all")
            self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show(self):
        """Testing that show exists"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup

        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show User " + user_id)
            x = (f.getvalue())

        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_show_class_name(self):
        """Testing the error messages for class name missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup

        with patch('sys.stdout', new=StribgIO()) as f:
            console.onecmd("show")
            x = (f.getvalue())

        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_show_class_name(self):
        """Test show message error for id missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup

        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show User")
            x = (f.getvalue())

        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    def test_show_no_instance_found(self):
        """Test show message error for id missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup

        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show User " + "124356876")
            x = (f.getvalue())

        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        """Test that create works"""
        console = self.create()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("create User")
            self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name_missing(self):
        """Testing the error messages for class name missing"""
        console = self.create()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("create")
            x = (f.getvalue())
            self.assertEqual("** class name missing **\n", x)

    def test_class_name_doest_exist(self):
        """Testing the error messages for class name missing"""
        console = self.create()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("create trudee")
            x = (f.getvalue())
            self.assertEqual("** class doesn't exist **\n", x)

    def test_destroy(self):
        console = self.create()
        result = console.onecmd("destroy")
        self.assertIsNone(result, "Destroy should complete successfully")

    def test_update(self):
        console = self.create()
        result = console.onecmd("update")
        self.assertIsNone(result, "update should complete successfully")


if __name__ == "__main__":
    unittest.main()
