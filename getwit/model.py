#QUERY PARAMETER
#TWEETS
def get_tweet_par(tweet_ids):
    return  {
            'ids': tweet_ids,
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,non_public_metrics,referenced_tweets,reply_settings,source,text,withheld',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'expansions': 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id',
            'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
            'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
            'media.fields': 'alt_text,duration_ms,height,media_key,non_public_metrics,organic_metrics,preview_image_url,promoted_metrics,public_metrics,type,url,width'
            }

def get_tweet_by_par():
    return  {
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,public_metrics,organic_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'expansions': 'attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id',
            'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
            'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
            'media.fields': 'duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text'
            }

#LIKES
def get_likes_lookup_par(max_results, pagination_token):
    return {
        'expansions': 'pinned_tweet_id',
        'max_results': max_results,
    #     'media.fields': 'duration_ms, height, media_key, preview_image_url, type, url, width, public_metrics, non_public_metrics, organic_metrics, promoted_metrics, alt_text',
        'pagination_token': pagination_token,
    #     'place.fields': 'contained_within, country, country_code, full_name, geo, id, name, place_type',
    #     'poll.fields': 'duration_minutes, end_datetime, id, options, voting_status',
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_liked_tweets_par(max_results, pagination_token):
    return {
        'expansions': 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id',
        'max_results': max_results,
        'media.fields': 'alt_text,duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width',
        'pagination_token': pagination_token,
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

#TIMELINE
def get_user_timeline_par():
    return {
        'exclude': 'replies,retweets',
        'expansions' : 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id',
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'media.fields': 'alt_text,duration_ms,height,media_key,non_public_metrics,organic_metrics,preview_image_url,public_metrics,type,url,width',
        'tweet.fields' : 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields' : 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld'
    }

def get_user_mention_timeline_par():
    return {
        'expansions' : 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id',
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'media.fields': 'alt_text,duration_ms,height,media_key,organic_metrics,preview_image_url,public_metrics,type,url,width',
        'tweet.fields' : 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields' : 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld'
    }

#USERS
def get_user_lookup_by_par(usernames):
    return {
            'usernames': usernames,
            'expansions': 'pinned_tweet_id',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld'
            }

def get_user_lookup_by_username_par():
    return {
            'expansions': 'pinned_tweet_id',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld'
            }

def get_users_lookup_par(user_ids):
    return {
            'ids': user_ids,
            'expansions': 'pinned_tweet_id',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld'
            }

def get_user_lookup_by_id_par():
    return {
            'expansions': 'pinned_tweet_id',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld'
            }

def get_my_par():
    return {
            'expansions': 'pinned_tweet_id',
            'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
            'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld'
            }

#SPACES
def get_spaces_by_id_par(space_id):
    return {
        'ids': space_id,
        'expansions' : 'host_ids,creator_id,invited_user_ids,speaker_ids,topic_ids',
        'topic.fields': 'description,id,name',
        'space.fields' : 'created_at,creator_id,ended_at,host_ids,id,invited_user_ids,is_ticketed,lang,participant_count,scheduled_start,speaker_ids,started_at,state,subscriber_count,title,topic_ids,updated_at',
        'user.fields' : 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld'
    }

def get_search_space_par(str_query):
    return {
        'query': str_query,
        'expansions' : 'host_ids,creator_id,invited_user_ids,speaker_ids,topic_ids',
        'state': 'all',
        #live,scheduled,all'
        'topic.fields': 'description,id,name',
        'space.fields' : 'created_at,creator_id,ended_at,host_ids,id,invited_user_ids,is_ticketed,lang,participant_count,scheduled_start,speaker_ids,started_at,state,subscriber_count,title,topic_ids,updated_at',
        'user.fields' : 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_spaces_par(space_ids):
    return {
        'ids': space_ids,
        'expansions' : 'host_ids,creator_id,invited_user_ids,speaker_ids,topic_ids',
        'topic.fields': 'id,name,description',
        'space.fields' : 'host_ids,created_at,creator_id,id,lang,invited_user_ids,participant_count,speaker_ids,started_at,ended_at,subscriber_count,topic_ids,state,title,updated_at,scheduled_start,is_ticketed',
        'user.fields' : 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_spaces_by_creator_ids_par(user_ids):
    return {
        'user_ids': user_ids,
        'expansions' : 'invited_user_ids,speaker_ids,creator_id,host_ids',
        'topic.fields': 'id,name,description',
        'space.fields' : 'created_at,creator_id,ended_at,host_ids,id,invited_user_ids,is_ticketed,lang,participant_count,scheduled_start,speaker_ids,started_at,state,subscriber_count,title,topic_ids,updated_at',
        'user.fields' : 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_spaces_buyers():
    return {
        'expansions': 'pinned_tweet_id',
        'media.fields': 'duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text',
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,public_metrics,organic_metrics,promoted_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_spaces_tweet():
    return {
        'expansions': 'attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id',
        'media.fields': 'duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text',
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,public_metrics,organic_metrics,promoted_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

#RETWEETS
def get_retweets_lookup_par(pagination_token):
    return {
        'expansions': 'pinned_tweet_id',
        # 'media.fields': 'duration_ms, height, media_key, preview_image_url, type, url, width, public_metrics, non_public_metrics, organic_metrics, promoted_metrics, alt_text',
        'pagination_token': pagination_token,
        # 'place.fields': 'id,max_results,pagination_token,expansions,tweet.fields,user.fields',
        # 'poll.fields' : 'id,max_results,pagination_token,expansions,tweet.fields,user.fields',
        'tweet.fields' : 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld'
    }

#SEARCH TWEETS
def get_recent_tweet_count_par(str_query):
    return {
        'query': str_query,
        'end_time': None,
        'granularity': 'day',
        #minute, hour or day
        'since_id': None,
        'start_time': None,
        'until_id': None
    }

def get_recent_search_par(str_query,end_time,max_results,next_token,since_id,start_time,until_id):
    return {
        'query': str_query,
        'end_time': end_time,
        #YYYY-MMMM-DDDDTHH:mm:ssZ
        'expansions': 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id',
        'max_results': max_results,
        'media.fields': 'alt_text,duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width',
        'next_token': next_token,
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'since_id': since_id,
        'start_time': start_time,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'until_id': until_id,
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

#QUOTE TWEETS
def get_quote_tweet_par(pagination_token):
    return {
        'expansions': 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id',
        'max_results': None,
        # 'media_fields': 'duration_ms, height, media_key, preview_image_url, type, url, width, public_metrics, non_public_metrics, organic_metrics, promoted_metrics, alt_text',
        'pagination_token': pagination_token,
        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
        'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld'
    }

#MUTES
def get_mutes_lookup_par(pagination_token):
    return {
        'expansions': 'pinned_tweet_id',
        'max_results': None,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

#LIST
def user_owned_list(max_results, pagination_token):
    return {
        'expansions': 'owner_id',
        'list.fields': 'created_at,description,follower_count,id,member_count,name,owner_id,private',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_list_lookup_par():
    return {
        'expansions': 'owner_id',
        'list.fields': 'created_at,description,follower_count,id,member_count,name,owner_id,private',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_pinned_list_par():
    return {
        'expansions': 'owner_id',
        'list.fields': 'created_at,description,follower_count,id,member_count,name,owner_id,private',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_list_membership_par(max_results, pagination_token):
    return {
        'expansions': 'owner_id',
        'list.fields': 'created_at,description,follower_count,id,member_count,name,owner_id,private',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_list_member_lookup_par(pagination_token, max_results):
    return {
        'expansions': 'pinned_tweet_id',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_user_list_followed_par(max_results, pagination_token):
    return {
        'expansions': 'owner_id',
        'list.fields': 'created_at,description,follower_count,id,member_count,name,owner_id,private',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_list_followers_lookup(max_results, pagination_token):
    return {
        'expansions': 'pinned_tweet_id',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

def get_list_tweets_par(max_results,pagination_token):
    return {
        'expansions': 'author_id',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

#FOLLOWS
def get_following_lookup_par(max_results, pagination_token):
    return {
        'expansions': 'pinned_tweet_id',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',

    }

def get_followers_lookup_par(max_results, pagination_token):
    return {
        'expansions': 'pinned_tweet_id',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld',
        'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
    }

#BLOCKS
def block_lookups_par(max_results, pagination_token):
    return {
        'expansion': 'pinned_tweet_id',
        'max_results': max_results,
        'pagination_token': pagination_token,
        'tweet.fields': 'attachments, author_id, context_annotations, conversation_id, created_at, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, public_metrics, organic_metrics, promoted_metrics, possibly_sensitive, referenced_tweets, reply_settings, source, text, withheld',
        'user.fields': 'created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, withheld',
    }

#endpoint khusus Twitterv2 Academic Reaserch
def full_archive_search_par(str_query, max_results):
    return {
        'query': str_query,
        'end_time': None,
        'expansion': 'attachments.poll_ids, attachments.media_keys, author_id, entities.mentions.username, geo.place_id, in_reply_to_user_id, referenced_tweets.id, referenced_tweets.id.author_id',
        'max_results': max_results,
        'media.fields': 'duration_ms, height, media_key, preview_image_url, type, url, width, public_metrics, alt_text',
    #   'next_token': '',
        'place.fields': 'contained_within, country, country_code, full_name, geo, id, name, place_type',
        'poll.fields': 'duration_minutes, end_datetime, id, options, voting_status',
    #   'since_id': ''
        'sort_order': 'recency',
        # relevancy
        'start_time': None,
        'tweet.fields': 'attachments, author_id, context_annotations, conversation_id, created_at, entities, geo, id, in_reply_to_user_id, lang, public_metrics, possibly_sensitive, referenced_tweets, reply_settings, source, text, withheld',
        'until_id': None,
        'user.fields': 'created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, withheld',
    }

def full_archive_tweet_count_par(str_query):
    return {
        'query': str_query,
        'end_time': None,
        'granularity': 'day',
        #minute, hour & day
    #   'next_token': '',
    #   'since_id': ''
        'until_id': None,
    }

# def create_compliance_job_par():
#     return {
#         'type': "tweet",
#         'name': "name",
#
#     }