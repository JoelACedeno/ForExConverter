from unittest import TestCase
from app import app

class TestApp(TestCase):

    def setUp(self):
    # set up testing client before every test
        self.app = app.test_client()

    def test_show_converter(self):
    # test that the show converter route works
        with self.app as client:
            res = client.get("/")
        
        self.assertEqual(res.status_code, 200)
    
    def test_valid_input(self):
    # test that the app handles valid data properly
        with self.app as client:
            res = client.post("/convert", data  = {
                "from_currency": "USD",
                "to_currency": "USD",
                "amount": "100"
            })
        
        self.assertEqual(res.status_code, 302)

        with client.session_transaction() as session:
        # test the session
            self.assertIn("from_currency", session)
            self.assertEqual(session["from_currency"], "USD")
            self.assertIn("to_currency", session)
            self.assertEqual(session["to_currency"], "USD")
            self.assertIn("amount", session)
            self.assertEqual(session["amount"], 100.00)
            self.assertIn("converted_amount", session)
            self.assertEqual(session["converted_amount"], 100.00)

    def test_invalid_input(self):
    # test the app handles invalid data properly
        with self.app as client:
            res = client.post("/convert", data = {
                "from_currency": "XYZ",
                "to_currency": "ABC",
                "amount": "invalid"
            })

        self.assertEqual(res.status_code, 200)
        with client.session_transaction() as session:
            self.assertNotIn("converted_amount", session)
        self.assertIn("Not a valid code: XYZ", str(res.data))
        self.assertIn("Not a valid code: ABC", str(res.data))
        self.assertIn("Invalid amount", str(res.data))

    def test_conversion(self):
    # test the app reroutes from /convert to /conversion properly
        with self.app as client:
            res = client.post("/convert", data  = {
                "from_currency": "USD",
                "to_currency": "USD",
                "amount": "1"
            })

        res = client.get("/conversion", follow_redirects = True)

        self.assertEqual(res.status_code, 200)

        # test that data is handled properly
        expected_result = "$1.00 USD is equal to $1.00 USD."
        self.assertIn(expected_result, str(res.data))
