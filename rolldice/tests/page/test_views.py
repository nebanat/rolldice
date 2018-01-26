from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        """Home page should respond with a status of 200"""
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """terms page should respond with a status of 200"""
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200
