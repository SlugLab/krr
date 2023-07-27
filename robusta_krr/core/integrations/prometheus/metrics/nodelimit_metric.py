from typing import Optional

from robusta_krr.core.models.allocations import ResourceType
from robusta_krr.core.models.objects import K8sObjectData

from .base_filtered_metric import BaseFilteredMetricLoader
from .base_metric import QueryType, bind_metric, override_metric


@bind_metric(ResourceType.NodeLimit1)
class NodeLimit1MetricLoader(BaseFilteredMetricLoader):
    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        return (
            "sum(container_rss_node_1{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}"
            "}) by (container, pod, job, id)"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.QueryRange


# This is a temporary solutions, metric loaders will be moved to strategy in the future
@override_metric("simple", ResourceType.NodeLimit1)
class SimpleNodeLimit1MetricLoader(NodeLimit1MetricLoader):
    """
    A class that overrides the NodeLimit1 metric on the simple strategy.
    """

    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        resolution_formatted = f"[{resolution}]" if resolution else ""
        return (
            f"max_over_time(container_rss_node_1{{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}}}"
            f"{resolution_formatted}"
            f")"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.Query

    def get_graph_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        return super().get_query(object, resolution)

@bind_metric(ResourceType.NodeLimit2)
class NodeLimit2MetricLoader(BaseFilteredMetricLoader):
    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        return (
            "sum(container_rss_node_2{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}"
            "}) by (container, pod, job, id)"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.QueryRange


# This is a temporary solutions, metric loaders will be moved to strategy in the future
@override_metric("simple", ResourceType.NodeLimit2)
class SimpleNodeLimit2MetricLoader(NodeLimit2MetricLoader):
    """
    A class that overrides the NodeLimit2 metric on the simple strategy.
    """

    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        resolution_formatted = f"[{resolution}]" if resolution else ""
        return (
            f"max_over_time(container_rss_node_2{{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}}}"
            f"{resolution_formatted}"
            f")"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.Query

    def get_graph_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        return super().get_query(object, resolution)

@bind_metric(ResourceType.NodeLimit3)
class NodeLimit3MetricLoader(BaseFilteredMetricLoader):
    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        return (
            "sum(container_rss_node_3{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}"
            "}) by (container, pod, job, id)"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.QueryRange


# This is a temporary solutions, metric loaders will be moved to strategy in the future
@override_metric("simple", ResourceType.NodeLimit3)
class SimpleNodeLimit3MetricLoader(NodeLimit3MetricLoader):
    """
    A class that overrides the NodeLimit3 metric on the simple strategy.
    """

    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        resolution_formatted = f"[{resolution}]" if resolution else ""
        return (
            f"max_over_time(container_rss_node_3{{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}}}"
            f"{resolution_formatted}"
            f")"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.Query

    def get_graph_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        return super().get_query(object, resolution)


@bind_metric(ResourceType.NodeLimit4)
class NodeLimit4MetricLoader(BaseFilteredMetricLoader):
    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        return (
            "sum(container_rss_node_4{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}"
            "}) by (container, pod, job, id)"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.QueryRange


# This is a temporary solutions, metric loaders will be moved to strategy in the future
@override_metric("simple", ResourceType.NodeLimit4)
class SimpleNodeLimit4MetricLoader(NodeLimit4MetricLoader):
    """
    A class that overrides the NodeLimit4 metric on the simple strategy.
    """

    def get_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        pods_selector = "|".join(pod.name for pod in object.pods)
        cluster_label = self.get_prometheus_cluster_label()
        resolution_formatted = f"[{resolution}]" if resolution else ""
        return (
            f"max_over_time(container_rss_node_4{{"
            f'namespace="{object.namespace}", '
            f'pod=~"{pods_selector}", '
            f'container="{object.container}"'
            f"{cluster_label}}}"
            f"{resolution_formatted}"
            f")"
        )

    def get_query_type(self) -> QueryType:
        return QueryType.Query

    def get_graph_query(self, object: K8sObjectData, resolution: Optional[str]) -> str:
        return super().get_query(object, resolution)
