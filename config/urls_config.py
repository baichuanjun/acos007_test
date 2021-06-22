# -*- coding:utf-8 -*-


class Urls(object):
    USER_LOGIN = "login"  #
    USER_INFO = "user_info"  #
    USER_RESET_PASSWORD = "reset_password"
    USER_REGISTER = "register"
    USER_LOGOUT = "logout"
    USER_IS_PHONE_REGISTERED = "is_phone_registered"
    USER_SEND_PHONE_CONFIRMATION_CODE = "send_phone_confirmation_code"
    USER_CONFIRM_PHONE_REGISTRATION_CONFIRMATION_CODE = "confirm_phone_registration_confirmation_code"
    USER_CONFIRM_PHONE_RESET_PASSWORD_CONFIRMATION_CODE = "confirm_phone_reset_password_confirmation_code"
    USER_PHONE_RESET_PASSWORD_CODE = "send_phone_reset_password_code"
    # 用户会员相关API，以及订单相关
    MEMBER_GET_ALL_MEMBERSHIP_PRODUCTS = "get_all_membership_products"
    ORDER_CREATE_ORDER = "create_order"
    ORDER_CREATE = "create_order"
    MEMBER_REDEEM_MEMBERSHIP = "redeem_membership"
    ORDER_ALIPAY_ORDER_NOTIFICATION = "alipay_order_notification"
    ORDER_GET_PAYMENT_URL = "get_payment_url"
    ORDER_GET_MY_ORDERS = "get_my_orders"
    ORDER_REQUEST_INVOICE = "request_invoice"
    ORDER_PAYMENT_STATUS = "payment_status"
    ORDER_GET_VALID_MEMBERSHIP = "get_valid_membership"
    # STORE
    STORE_UPDATE = "update_store"
    # STORE_DELETE = "delete_store"
    STORE_CREATE = "create_store"
    STORE_GET_ALL_STORES = "get_all_stores"
    STORE_UPLOAD = "upload"
    STORE_BIND_STORE = "bind_store"
    STORE_VALIDATE_BIND_ID = "validate_bind_id"
    STORE_GET_NEW_BIND_ID = "get_new_bind_id"
    STORE_GET_BIND_DATA = "get_bind_data"
    # report
    REPORT_GET_CHART_REPORTS = "get_chart_reports"
    # campaigns
    CAMPAIGNS_GET_CAMPAIGNS = "get_campaigns"
    CAMPAIGNS_GET_CAMPAIGN = "get_campaign"
    CAMPAIGNS_CREATE_CAMPAIGNS = "create_campaigns"
    # CAMPAIGNS_DELETE_CAMPAIGN = "delete_campaign"
    CAMPAIGNS_UPDATE_CAMPAIGNS = "update_campaigns"
    # group
    GROUP_GET_AD_GROUPS = "get_ad_groups"
    GROUP_GET_AD_GROUP = "get_ad_group"
    GROUP_CREATE_AD_GROUPS = "create_ad_groups"
    GROUP_UPDATE_AD_GROUPS = "update_ad_groups"
    # GROUP_DELETE_AD_GROUP = "delete_ad_group"
    # keyword
    KEYWORD_GET_KEYWORD = "get_keyword"
    KEYWORD_GET_KEYWORDS = "get_keywords"
    KEYWORD_CREATE_KEYWORDS = "create_keywords"
    # KEYWORD_DELETE_KEYWORD = "delete_keyword"
    KEYWORD_UPDATE_KEYWORDS = "update_keywords"
    KEYWORD_KEYWORDS_TRANSLATIONS = "keywords_translations"
    # negative_keyword
    NEGATIVE_KEYWORD_GET_NEGATIVE_KEYWORD = "get_negative_keyword"
    NEGATIVE_KEYWORDS_GET_NEGATIVE_KEYWORDS = "get_negative_keywords"
    NEGATIVE_KEYWORDS_CREATE = "create_negative_keywords"
    # NEGATIVE_KEYWORD_DELETE = "delete_negative_keyword"
    NEGATIVE_KEYWORDS_UPDATE = "update_negative_keywords"
    # BidRecommendations
    BID_RECOMMENDATIONS_GET_KEYWORDS = "get_bid_recommendations_keywords"
    BID_RECOMMENDATIONS_GET_GROUP = "get_bid_recommendation_adgroup"
    BID_RECOMMENDATIONS_GET_KEYWORD = "get_bid_recommendation_keyword"
    BID_RECOMMENDATIONS_GET_TARGETS = "get_bid_recommendation_targets"
    # product_ads
    PRODUCT_AD_GET = "get_product_ad"
    PRODUCT_ADS_GET = "get_product_ads"
    PRODUCT_ADS_CREATE = "create_product_ads"
    # PRODUCT_AD_DELETE = "delete_product_ad"
    PRODUCT_ADS_UPDATE = "update_product_ads"

    # Product targeting
    TARGETS_CREATE = "create_targets"
    TARGETS_UPDATE = "update_targets"
    TARGETS_GET = "get_targets"
    TARGET_GET = "get_target"
    # TARGET_DELETE = "delete_target"

    # CATEGORIES
    CATEGORIES_GET_AMAZON_CATEGORIES = "get_amazon_categories"
    CATEGORIES_GET_TARGET_CATEGORIES = "get_target_categories"
    CATEGORIES_GET_TARGET_CATEGORY_REFINEMENTS = "get_target_category_refinements"
    CATEGORIES_GET_TARGET_PRODUCT_RECOMMENDATIONS = "get_target_product_recommendations"
    # campaigns negative keywords
    CAMPAIGNS_NEGATIVE_KEYWORD_GET = "get_campaign_negative_keyword"
    # CAMPAIGNS_NEGATIVE_KEYWORD_DELETE = "delete_campaign_negative_keyword"
    CAMPAIGNS_NEGATIVE_KEYWORDS_GET = "get_campaign_negative_keywords"
    CAMPAIGNS_NEGATIVE_KEYWORDS_CREATE = "create_campaign_negative_keywords"
    CAMPAIGNS_NEGATIVE_KEYWORDS_UPDATE = "update_campaign_negative_keywords"
    # portfolios
    PORTFOLIOS_GET = "get_portfolios"
    PORTFOLIO_GET = "get_portfolio"
    PORTFOLIO_CREATE = "create_portfolios"
    PORTFOLIO_UPDATE = "update_portfolios"
    # Negative product targeting
    PRODUCT_NEGATIVE_PRODUCT_TARGETINGS_GET = "get_negative_product_targetings"
    PRODUCT_NEGATIVE_PRODUCT_TARGETING_GET = "get_negative_product_targeting"
    PRODUCT_NEGATIVE_PRODUCT_TARGETING_CREATE = "create_negative_product_targeting"
    # PRODUCT_NEGATIVE_PRODUCT_TARGETING_DELETE = "delete_negative_product_targeting"
    PRODUCT_NEGATIVE_PRODUCT_TARGETING_UPDATE = "update_negative_product_targeting"

    # Suggested keywords
    SUGGESTED_KEYWORDS_FOR_ASIN = "get_suggested_keyword_asin"
    SUGGESTED_KEYWORDS_FOR_ADGROUP = "get_suggested_keyword_adgroup"
    SUGGESTED_KEYWORDS_FOR_ASINS = "get_suggested_keywords_asins"
    # product
    PRODUCTS_GET_STORE_PRODUCTS = "get_store_products"
    PRODUCTS_GET_STORE_DATA_FOR_ASIN = "get_product_data_for_asins"
    PRODUCTS_SEARCH_AMAZON_PRODUCT_BY_ASIN = "search_amazon_product_by_asin"
    # amazon order
    AMAZON_ORDERS_GET = "get_amazon_orders"
    AMAZON_ORDER_GET = "get_order"

    # root store
    ROOT_STORES_GET_ALL_STORES = "root/get_all_stores"
    # root memberships
    ROOT_MEMBERSHIP_GET_PRODUCT = "root/create_membership_product"
    ROOT_MEMBERSHIP_UPDATE_PRODUCT = "root/update_membership_product"
    # ROOT_MEMBERSHIP_DELETE_PRODUCT = "root/delete_membership_product"
    # root referral
    ROOT_REFERRAL_CREATE = "root/create_referral"
    ROOT_REFERRAL_UPDATE = "root/update_referral"
    # ROOT_REFERRAL_DELETE = "root/delete_referral"
    ROOT_REFERRALS_GET = "root/get_all_referrals"
    # referral reward
    ROOT_REFERRAL_REWARDS_GET = "root/get_referral_rewards"
    ROOT_REFERRAL_REWARD_CREATE = "root/create_referral_reward"
    ROOT_REFERRAL_REWARD_UPDATE = "root/update_referral_reward"
    # ROOT_REFERRAL_REWARD_DELETE = "root/delete_referral_reward"

    REFERRAL_REWARD_GET = "get_referral_reward"
    ROOT_REDEEM_CODES_GET_ALL = "root/get_all_redeem_codes"
    # ROOT_REDEEM_CODE_DELETE = "root/delete_redeem_code"
    ROOT_REDEEM_CODE_UPDATE = "root/update_redeem_code"


class NullClass(object):
    """
    TODO 不要删除该空类 也不要修改此空类 !!!!
    """
    pass
