def test_signup_adds_participant_to_activity(client):
    """Test that signup successfully adds participant to activity."""
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    assert email in response.json()["message"]


def test_signup_response_format(client):
    """Test that signup returns message in expected format."""
    # Arrange
    activity = "Programming Class"
    email = "testuser@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)


def test_signup_duplicate_participant_rejected(client):
    """Test that duplicate signup is rejected."""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # Already registered
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_activity_not_found(client):
    """Test that signup fails for non-existent activity."""
    # Arrange
    activity = "Nonexistent Activity"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
