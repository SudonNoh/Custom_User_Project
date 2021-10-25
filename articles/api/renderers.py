from core.renderers import CoreJSONRenderer


class ArticleJSONRenderer(CoreJSONRenderer):
    object_label = 'article'
    # object_label_plural = 'articles'
    pagination_object_label = 'articles'
    pagination_object_count = 'articlesCount'
    
    
class CommentJSONRenderer(CoreJSONRenderer):
    object_label = 'comment' 
    # object_label_plural = "comments"
    pagination_object_label = 'comments'
    pagination_object_count = 'commentsCount'