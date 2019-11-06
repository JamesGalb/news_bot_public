# -*- coding: utf-8 -*-
import sys
import logging
import traceback
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .spiders.youtube import YoutubeSpider
from .spiders.donaldjtrump import DonaldjtrumpSpider
from .spiders.twitter import TwitterSpider
from .spiders.dhs_gov import DHSGovSpider
from .spiders.commerce_gov import CommerceGovSpider
from .spiders.defense_gov import DefenseGovSpider
from .spiders.education_gov import EducationGovSpider
from .spiders.usda_gov import USDAGovSpider
from .spiders.energy_gov import EnergyGovSpider
from .spiders.hhs_gov_news import HHSGovNewsSpider
from .spiders.hhs_gov_blog import HHSGovBlogSpider
from .spiders.state_gov import StateGovSpider
from .spiders.hud_gov import HUDGovSpider
from .spiders.justice_gov import JusticeGovSpider
from .spiders.dol_gov import DOLGovSpider
from .spiders.transportation_gov import TransportationGovSpider
from .spiders.va_gov import VAGovSpider
#from .spiders.doi_gov import DOIGovSpider
from .spiders.treasury_gov import TreasuryGovSpider
from .spiders.treasury_stories_gov import TreasuryStoriesGovSpider
from .spiders.cia_gov import CIAGovSpider
from .spiders.epa_gov import EPAGovSpider
from .spiders.dni_gov import DNIGovSpider
from .spiders.sba_gov import SBAGovSpider
from .spiders.sec_gov import SECGovSpider
from .spiders.west_wing_reads import WestWingReadsSpider
from .spiders.fbi_gov import FBIGovSpider
from .spiders.whitehouse_news import WhitehouseNewsSpider
from .spiders.gop_spider import GOPSpider
from .spiders.cbp_gov import CBPGovSpider
from .spiders.joint_chiefs_gov import JointChiefsSpider
from .spiders.bls_gov import BLSGovSpider
from .spiders.bls_gov_announcement import BLSGovAnnouncementSpider
from .spiders.bls_gov_ted import BLSGovTEDSpider
from .spiders.usun_gov import USUNGovSpider
from .spiders.oig_gov import OIGGovSpider
from .spiders.justice_gov_blog import JusticeGovBlogSpider
from .spiders.oversight_gov import OversightGovSpider
from .spiders.ignet_gov import IGNetGovSpider
#from .spiders.facebook import FacebookSpider
from .spiders.daily1600 import Daily1600Spider
from .spiders.daily1600video import Daily1600videoSpider
from .spiders.daily1600pic import Daily1600picSpider
from .spiders.nasa_gov import NASAGovSpider
from .spiders.ice_gov import ICEGovSpider
from .spiders.uscis_gov import USCISGovSpider
from .spiders.space_comm_gov import SpaceCommGovSpider
from .spiders.usaid_gov import USAidGovSpider
from .spiders.cbp_rss_gov import CBPrssGovSpider
#from .spiders.gop_research import GOPResearchSpider
from .spiders.space_air_force import SpaceAirForceSpider


class SpiderRunner():
    def __init__(self):
        self.SPIDER_LIST = [
            TwitterSpider, YoutubeSpider, DHSGovSpider, DonaldjtrumpSpider, CommerceGovSpider, DefenseGovSpider, NASAGovSpider, SpaceCommGovSpider,
            EducationGovSpider, USDAGovSpider, EnergyGovSpider, HHSGovNewsSpider, HUDGovSpider, DOLGovSpider, OIGGovSpider, JusticeGovBlogSpider,
            HHSGovBlogSpider, JusticeGovSpider, GOPSpider, CBPGovSpider, JointChiefsSpider, USUNGovSpider, OversightGovSpider, IGNetGovSpider, CBPrssGovSpider,
            TransportationGovSpider, VAGovSpider, StateGovSpider, USAidGovSpider, USCISGovSpider, ICEGovSpider, SpaceAirForceSpider,
            TreasuryGovSpider, TreasuryStoriesGovSpider, CIAGovSpider, EPAGovSpider, DNIGovSpider, SBAGovSpider, SECGovSpider,
            FBIGovSpider, WhitehouseNewsSpider, WestWingReadsSpider, BLSGovSpider, BLSGovAnnouncementSpider, BLSGovTEDSpider, Daily1600Spider, Daily1600videoSpider, Daily1600picSpider
        ]

        # This array does nothing
        # It's just to keep track of which spiders need to be worked on
        brokenSpiders = [
            ##DOLGovBlogSpider - Dont need, havent repaired
            ##DOIGovSpider - Cant get to work
            ##FacebookSpider Trump Videos 
            ##GOPResearchSpider
             
        ]

#Need to change Pipeline information
    def run_spiders(self):
        #Crawl feeds for new URLs.  Add to DB in pipeline if not in existing URLs
        try:
            ## set up the crawler and start to crawl one spider at a time
            process = CrawlerProcess(settings={'SCRAPE_LIMIT': 6,
                                       'LOG_LEVEL': 'DEBUG',
                                       'USER_AGENT': 'JamesGalb (+https://www.reddit.com/r/Donald_Trump)',
                                       'ROBOTSTXT_OBEY': False,
                                       'ITEM_PIPELINES': { 'news_releases.pipelines.MySQLPipeline': 300 },
                                       'DOWNLOAD_TIMEOUT': 12,
                                       'DNS_TIMEOUT': 12,
                                       'RETRY_ENABLED': False
                                       })
            for spider in self.SPIDER_LIST:
                process.crawl(spider)
            process.start()
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.info('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            logging.info("Exception: %s" % str(traceback.format_exc()))


    def get_spider_list(self):
        return self.SPIDER_LIST
