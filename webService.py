__author__ = 'Scott'

#Team/Group imports
import datetime
import ebayFinder
from Kerb_Auth_Check import auth_kinit
import logging
import web
##import SQLConnection
from wsLogging import Log

#WebPy imports
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types

logging.basicConfig(filename="service.log", level="DEBUG")

urls = ("/ebay", "EbayServ",
        "/ebay.wsdl", "EbayServ",
        )
render = web.template.Template("$def with (var)\n$:var")

##Processing and login is in the class
class SoapService(SimpleWSGISoapApp):
    """Class for webservice """
    ##Login method
    try:
        @soapmethod(soap_types.String, soap_types.String, _returns=soap_types.Boolean)
        def service_login(self,username, password):
           # logging.info("Login attempted {}",datetime.datetime.now())
            if auth_kinit(username, password) == True:
                logging.info("Successful Login {}",datetime.datetime.now())
            else:
                logging.info("Login Failed {}",datetime.time.now())
                return False
    except TypeError:
        logging.error("There was a type error")
    except:
        logging.error("Some other error occurred")


    #if does_ticket_exist() == True:
    # @soapmethod(soap_types.String, _returns=soap_types.String)
    # def ebay_service(self,keyword):
    #     return ebayFinder.itemFinder(keyword)

#Methods here are for how web service communicates
class EbayServ(SoapService):
    """Class for web.py """
    def start_response(self, status, headers):
        web.ctx.status = status
        for header, value in headers:
            web.header(header, value)

    def GET(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

    ##Primary method
    def POST(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))


#Tells web app to start, gives urls
app=web.application(urls, globals())

if __name__ == "__main__":
    app.run()
    wsLogging.run(Log)
