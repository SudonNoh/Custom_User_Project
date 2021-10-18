from core.renderers import CoreJSONRenderer


class ArticleJSONRenderer(CoreJSONRenderer):
    object_label = 'article'
    object_label_plural = 'articles'