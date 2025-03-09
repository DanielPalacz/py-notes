from unittest.mock import Mock

# Create a mock object
email_service = Mock()

# Define expected behavior
email_service.send_email.return_value = "Email sent successfully"

# Call the method
response = email_service.send_email("john.doe@example.com")

# Verify behavior
email_service.send_email.assert_called_with("john.doe@example.com")
assert response == "Email sent successfully"
