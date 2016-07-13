from wr_common import Print, clean_spaces, w
import socket
import urllib
import requests
import lxml.html
# from lxml.html.clean import Cleaner
from xml.dom.minidom import parse
import randua

import HTMLParser
h = HTMLParser.HTMLParser()

regexpNS = "http://exslt.org/regular-expressions"
namespaces = {'re': regexpNS}

def wait_for_connection(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    while 1:
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except Exception as ex:
            print 'No Internet Connection! Wait 3 seconds and try again!'
            sleep(3)

def Resp(url, headers={'User-Agent' : randua.generate() }):
    no_resp_count = 0
    while 1:
        try:
            resp = requests.get(url)
        except Exception as e:
            print type(e), e

            if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
                wait_for_connection()
                continue

            time.sleep(1)

        else:
            if resp and resp.ok:
                source = resp.text
                doc = lxml.html.document_fromstring(source)

                return (source, doc)
            else:
                print 'no resp'
                no_resp_count += 1
                if no_resp_count == 10:
                    return (False, False) 

def RespJSON(url, headers={'User-Agent' : randua.generate() }):
    no_resp_count = 0
    while 1:
        try:
            resp = requests.get(url, headers)
        except Exception as e:
            print type(e), e

            if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
                wait_for_connection()
                continue

            time.sleep(1)                

        else:
            if resp and resp.ok:
                try:
                    json_data = resp.json()
                except Exception as err:
                    print type(err, err)
                    time.sleep(1)
                else:
                    return json_data
            else:
                print 'no resp'
                no_resp_count += 1
                if no_resp_count == 10:
                    return False

def RespXML(url, headers={'User-Agent' : randua.generate() }):
    no_resp_count = 0
    while 1:
        try:
            resp = requests.get(url)
        except Exception as e:
            print type(e), e

            if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
                wait_for_connection()
                continue

            time.sleep(1)

        else:
            if resp and resp.ok:
                source = resp.content
                return source
            else:
                print 'no resp'
                no_resp_count += 1
                if no_resp_count == 10:
                    return False

def DownloadFile(url, path):
    no_resp_count = 0
    while 1:
        try:
            resp = requests.get(url)
        except Exception as e:
            print type(e), e

            if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
                wait_for_connection()
                continue

            time.sleep(1)

        else:
            if resp and resp.ok:
                f = open(path, 'wb')
                f.write(resp.content)
                f.close() 
                return True

            else:
                print 'no resp'
                no_resp_count += 1
                if no_resp_count == 10:
                    return False

def DownloadBigFile(url, path):
    no_resp_count = 0
    while 1:
        try:
            with open(path, 'wb') as handle:
                resp = requests.get(url, stream=True)

                if not resp.ok:
                    return False

                for block in resp.iter_content(1024):
                    handle.write(block)

        except Exception as err:
            print type(err), err, url
        else:
            return True
                   

def Field(field_dict, doc, names, XPath):
    field = doc.xpath(XPath)
    if field:
        field = ''.join(field)
        field = ' '.join(field.split())

        if field:
            for name in names.split(','):
                name = clean_spaces(name)
                # Print(name, field)
                field_dict[name] = field

            return field  

    return False

# XPath "not equal" function
def not_equal(array, attr_name):
    for i in range(len(array)):
        array[i] = 'not(@' + attr_name + '="' + array[i] + '")'

    return ' and '.join(array)

# XPath "not contains" function
def not_contains(array, attr_name):
    for i in range(len(array)):
        array[i] = 'not(contains(@' + attr_name + ', "' + array[i] + '"))'

    return ' and '.join(array)

# XPath "contains" function
def contains(array, attr):
    for i in range(len(array)):
        array[i] = 'contains(' + attr + ', "' + array[i] + '")'

    return ' or '.join(array)    

def get_first_tag_text(xml, tag_name):
    dom = parse(xml)
    name = dom.getElementsByTagName(tag_name)
    if name:
        return name[0].firstChild.nodeValue   
    else:
        return False