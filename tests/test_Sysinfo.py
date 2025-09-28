import pytest
from Commands.sysinfo import get_sysinfo, get_dashboard

def test_sysinfo_fields_exist():
    data = get_sysinfo()
    keys = [
        "os", "kernel", "hostname", "uptime",
        "cpu", "cores", "threads", "gpu",
        "ram_used", "ram_total", "swap_used", "swap_total",
        "disk_used", "disk_total", "disk_free", "disk_percent",
        "ip"
    ]
    for key in keys:
        assert key in data

def test_field_types():
    data = get_sysinfo()
    assert isinstance(data['os'], str)
    assert isinstance(data['kernel'], str)
    assert isinstance(data['hostname'], str)
    assert isinstance(data['uptime'], str)
    assert isinstance(data['cpu'], str)
    assert isinstance(data['cores'], int)
    assert isinstance(data['threads'], int)
    assert isinstance(data['gpu'], str)
    assert isinstance(data['ram_used'], str)
    assert isinstance(data['ram_total'], str)
    assert isinstance(data['swap_used'], str)
    assert isinstance(data['swap_total'], str)
    assert isinstance(data['disk_used'], str)
    assert isinstance(data['disk_total'], str)
    assert isinstance(data['disk_free'], str)
    assert isinstance(data['disk_percent'], str)
    assert isinstance(data['ip'], str)

def test_dashboard_output_contains_data():
    data = get_sysinfo()
    dash = get_dashboard(data)
    assert data['cpu'] in dash
    assert data['gpu'] in dash
    assert data['ram_used'] in dash
    assert data['ram_total'] in dash
    assert data['disk_used'] in dash
    assert data['disk_total'] in dash
    assert data['ip'] in dash

def test_values_format():
    data = get_sysinfo()
    assert data['ram_used'].endswith("GB")
    assert data['ram_total'].endswith("GB")
    assert data['swap_used'].endswith("GB") or data['swap_used'].endswith("B")
    assert data['swap_total'].endswith("GB")
    assert data['disk_used'].endswith("GB")
    assert data['disk_total'].endswith("GB")
    assert "%" in data['disk_percent']
    uptime_parts = data['uptime'].split()
    assert all(any(c.isdigit() for c in part) for part in uptime_parts)

def test_no_empty_strings():
    data = get_sysinfo()
    for k, v in data.items():
        assert v is not None
        assert v != ""