def test_unregister_removes_participant(client):
    """Test that unregister successfully removes participant from activity."""
    # Arrange
    activity = "Gym Class"
    email = "john@mergington.edu"  # Known participant
    
    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]


def test_unregister_response_format(client):
    """Test that unregister returns message in expected format."""
    # Arrange
    activity = "Gym Class"
    email = "olivia@mergington.edu"  # Known participant
    
    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)


def test_unregister_participant_not_found(client):
    """Test that unregister fails for non-existent participant."""
    # Arrange
    activity = "Chess Club"
    email = "notexist@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"


def test_unregister_activity_not_found(client):
    """Test that unregister fails for non-existent activity."""
    # Arrange
    activity = "Nonexistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
