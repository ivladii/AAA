from tests.code.what_is_year_now import what_is_year_now
from unittest.mock import patch
import json
import io
from urllib.error import HTTPError
import pytest


class TestYearNow:

    @patch('urllib.request.urlopen', io.StringIO)
    def test_dt_sep_hyp(self):
        fake_api_url = '{"currentDateTime": "2010-11-30 01:06:37.923098"}'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            year = what_is_year_now()

        exp_year = 2010

        assert year == exp_year

    @patch('urllib.request.urlopen', io.StringIO)
    def test_dt_sep_dot(self):
        fake_api_url = '{"currentDateTime": "30.11.2020 01:06:37.923098"}'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            year = what_is_year_now()
        exp_year = 2020

        assert year == exp_year

    @patch('urllib.request.urlopen', io.StringIO)
    def test_raise_not_key(self):
        fake_api_url = '{"DateTime": "30.11.2020 01:06:37.923098"}'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            with pytest.raises(KeyError):
                what_is_year_now()

    @patch('urllib.request.urlopen', io.StringIO)
    def test_raise_not_sep(self):
        fake_api_url = '{"currentDateTime": "30/11/2020 01:06:37.923098"}'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            with pytest.raises(ValueError):
                what_is_year_now()

    @patch('urllib.request.urlopen', io.StringIO)
    def test_return_int(self):
        fake_api_url = '{"currentDateTime": "30.11.2020 01:06:37.923098"}'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
            year = what_is_year_now()

        assert isinstance(year, int)

    @patch('urllib.request.urlopen', io.StringIO)
    def test_raise_response_not_json(self):
        fake_api_url = '"currentDateTime": "30/11/2020 01:06:37.923098"'
        with patch('tests.code.what_is_year_now.API_URL', fake_api_url):
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
