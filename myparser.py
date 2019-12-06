from bs4 import BeautifulSoup
from result import Result

class Parser:

    PARSER = 'lxml'

    def parse_urls(self, resource):
        """Parses clean urls out of HTML resource
        
        Args:
            resource: HTML resource as a string

        Returns:
            List of clean urls as strings

        Raises:
            SumSoupError: Maybe if BS doesn't work or something
        """


        soup = BeautifulSoup(resource, self.PARSER)

        parsed_urls = []
        urls = soup.find_all('div', class_='result-link')

        for url in urls:
            parsed_url = url.find('a')['href']
            if parsed_url not in parsed_urls:
                parsed_urls.append(parsed_url)

        return parsed_urls

    
    def parse_results(self, resource):
        """Parses text from web page
        
        Ge

        Args:
            resource: HTML resource as a string

        Returns
            List of Result objects
            
        Raises:
            SumSoupError: Maybe if BS doesn't work or something (TypeError?)
        """


        output = []
        soup = BeautifulSoup(resource, self.PARSER)

        question = soup.find('div', id='question')
        q_votes = question.find('div', class_='votecell').getText().replace('\n', ' ').strip().split(' ')[0]
        q_text = question.find('div', class_='post-text').getText().replace('\n', ' ').strip()
        q_info_container = question.find('div', class_='post-signature owner grid--cell')
        q_date = q_info_container.find('span', class_='relativetime').getText().replace('\n', ' ').strip()
        q_user = q_info_container.find('div', class_='user-details').find('a').getText().replace('\n', ' ').strip()

        q = Result([{'type': 'text', 'content': q_text}], q_user, q_votes, q_date)
        output.append(q)

        answers = soup.find_all('div', class_='answer')

        # TODO: clean up this shit
        for answer in answers:
            all_text = None
            a_user = None
            a_votes = None
            a_date = None

            a_votes = answer.find('div', class_='votecell').getText().replace('\n', ' ').strip().split(' ')[0]
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
                pass

            try:
                a_date = a_info_container.find('span', class_='relativetime').getText().replace('\n', ' ').strip()
            except:
                pass    

            all_text = []
            a_text = answer.find('div', class_='post-text')
            for elem in a_text:
                if elem.name == 'pre':
                    all_text.append({'type': 'code', 'content': elem.text.split('\n')})
                elif elem.name == 'p':
                    all_text.append({'type': 'text', 'content': elem.text.replace('\n', ' ').strip()})
                # elif elem.name == 'h1':
                #     all_text.append({'type': 'heading', 'content': elem.text})

            a = Result(all_text, a_user, a_votes, a_date)
            output.append(a)

        return output