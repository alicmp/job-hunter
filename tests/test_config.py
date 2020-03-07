import os


def test_config():
    """Check whether if all necessary configs are in env file or not"""
    assert os.environ.get('reddit_personal_use_script') is not None
    assert os.environ.get('reddit_secret') is not None
    assert os.environ.get('reddit_app_name') is not None
    assert os.environ.get('reddit_username') is not None
    assert os.environ.get('reddit_passwrod') is not None
