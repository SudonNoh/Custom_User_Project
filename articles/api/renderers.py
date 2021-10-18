from core.renderers import CoreJSONRenderer


class ArticleJSONRenderer(CoreJSONRenderer):
    object_label = 'article'
    object_label_plural = 'articles'
    
    
class CommentJSONRenderer(CoreJSONRenderer):
    object_label = 'comment' 
    object_label_plural = "comments"