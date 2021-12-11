from tests.code.what_is_year_now import what_is_year_now
from unittest.mock import patch
import json
import io
from urllib.error import HTTPError
import pytest


class TestYearNow:

    def test_dt_sep_hyp(self):
        response = '{"currentDateTime": "2010-11-30 01:06:37.923098"}'
        with patch('urllib.request.urlopen', return_value=io.StringIO(response)):
            year = what_is_year_now()

        exp_year = 2010

        assert year == exp_year

    def test_dt_sep_dot(self):
        response = '{"currentDateTime": "30.11.2020 01:06:37.923098"}'
        with patch('urllib.request.urlopen', return_value=io.StringIO(response)):
            year = what_is_year_now()
        exp_year = 2020

        assert year == exp_year

    def test_raise_not_key(self):
        response = '{"DateTime": "30.11.2020 01:06:37.923098"}'
        with patch('urllib.request.urlopen', return_value=io.StringIO(response)):
            with pytest.raises(KeyError):
                what_is_year_now()

    def test_raise_not_sep(self):
        response = '{"currentDateTime": "30/11/2020 01:06:37.923098"}'
        with patch('urllib.request.urlopen', return_value=io.StringIO(response)):
            with pytest.raises(ValueError):
                what_is_year_now()

    def test_return_not_int(self):
        response = '{"currentDateTime": "первое / февраль / двадцать первый"}'
        with patch('urllib.request.urlopen', return_value=io.StringIO(response)):
            with pytest.raises(ValueError):
                what_is_year_now()

    def test_raise_response_not_json(self):
        response = '"currentDateTime": "30/11/2020 01:06:37.923098"'
        with patch('urllib.request.urlopen', return_value=io.StringIO(response)):
            with pytest.raises(json.JSONDecodeError):
                what_is_year_now()

    def test_raise_bad_url(self):
        fake_api_url = 'url_with_out_http'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            with pytest.raises(ValueError):
                what_is_year_now()

    def test_raise_404(self):
        fake_api_url = 'http://worldclockapi.com/api/json/utc'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            with pytest.raises(HTTPError):
                what_is_year_now()


if __name__ == '__main__':
    pytest.main()
