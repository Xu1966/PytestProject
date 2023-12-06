import datetime
import pytest

if __name__ == '__main__':
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"test_report_{timestamp}.html"

    pytest.main([
        "NotesTest",
        f"--html={report_file}",
    ])
