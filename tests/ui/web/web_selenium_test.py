
MOCKUP_VIDEO = "/resources/dmytro_69_video.Y4M"

def test_webcam(app):
    app.open_app()

    app.test_camera()

    app.check_video()

    app.capture_screenshot("dima")

    camera_name = app.get_camera_name()

    expected_name = app.get_tests_dir_pat() + MOCKUP_VIDEO
    print("--> expected_name=" + expected_name)

    assert camera_name == expected_name
