from bs4 import BeautifulSoup
from config import Config
from result import Result


class Parser:
    """Class used for parsing wanted information from HTML"""


    def parse_urls(self, resource):
        """Parses clean urls out of HTML resource
        
        Args:
            resource: HTML resource as a string

        Returns:
            List of clean urls as strings
        """


        soup = BeautifulSoup(resource, Config.PARSER)

        parsed_urls = []
        urls = soup.find_all('div', class_='result-link')

        for url in urls:
            parsed_url = url.find('a')['href']
            if parsed_url not in parsed_urls:
                parsed_urls.append(parsed_url)

        return parsed_urls

    
    def parse_results(self, url, resource):
        """Parses results from single results thread

        Args:
            resource: HTML resource as a string

        Returns
            List of Result objects
        """


        output = []
        soup = BeautifulSoup(resource, Config.PARSER)

        # TODO: Parse the question as own function
        question = soup.find('div', id='question')
        q_votes = question.find('div', class_='votecell').getText().replace('\n', ' ').strip().split(' ')[0]
        q_text = question.find('div', class_='post-text').getText().replace('\n', ' ').strip()
        q_info_container = question.find('div', class_='post-signature owner grid--cell')
        q_date = q_info_container.find('span', class_='relativetime').getText().replace('\n', ' ').strip()
        q_user = q_info_container.find('div', class_='user-details').find('a').getText().replace('\n', ' ').strip()

        q = Result(url, [{'type': 'text', 'content': q_text}], q_user, q_votes, q_date)
        output.append(q)

        # TODO: Parse the answers as own function
        answers = soup.find_all('div', class_='answer')

        for answer in answers:
            try:
                a_votes = answer.find('div', class_='votecell').getText().replace('\n', ' ').strip().split(' ')[0]
            except:
                a_votes = 'N/A'

            try:
                a_info_container = answer.find_all('div', class_='post-signature grid--cell fl0')
                if len(a_info_container) > 1:
                    a_info_container = a_info_container[1]
                else:
                    a_info_container = a_info_container[0]
            except:
                pass

            try:
                a_user = a_info_container.find('div', class_='user-details').find('a').getText().replace('\n', ' ').strip()
            except:
                a_user = 'N/A'

            try:
                a_date = a_info_container.find('span', class_='relativetime').getText().replace('\n', ' ').strip()
            except:
                a_date = 'N/A'
                   
            try:
                all_text = []
                a_text = answer.find('div', class_='post-text')
                for elem in a_text:
                    if elem.name == 'pre':
                        all_text.append({'type': 'code', 'content': elem.text.split('\n')})
                    elif elem.name == 'p':
                        all_text.append({'type': 'text', 'content': elem.text.replace('\n', ' ').strip()})
                    # elif elem.name == 'h1':
                    #     all_text.append({'type': 'heading', 'content': elem.text})
            except:
                all_text = ['N/A']

            a = Result(url, all_text, a_user, a_votes, a_date)
            output.append(a)

        return output