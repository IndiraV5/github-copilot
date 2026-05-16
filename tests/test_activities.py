def test_get_activities_returns_dict(client):
    """Test that GET /activities returns activities dictionary."""
    # Arrange
    expected_activities = ["Chess Club", "Programming Class", "Gym Class"]
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    
    # Assert
    assert response.status_code == 200
    assert isinstance(activities, dict)
    assert all(name in activities for name in expected_activities)


def test_activities_have_required_fields(client):
    """Test that each activity has required fields."""
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    
    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in activities.items():
        assert all(field in activity_data for field in required_fields)
        assert isinstance(activity_data["participants"], list)
        assert isinstance(activity_data["max_participants"], int)
