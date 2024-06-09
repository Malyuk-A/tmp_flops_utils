import dataclasses

from flops_utils.types import CustomEnum


class Target(CustomEnum):
    FLOPS_MANAGER = "flops_manager"
    PROJECT_OBSERVER = "project_observer"


class Subject(CustomEnum):
    PROJECT_OBSERVER = "project_observer"
    FL_ACTORS_IMAGE_BUILDER = "fl_actors_image_builder"
    TRAINED_MODEL_IMAGE_BUILDER = "trained_model_image_builder"
    AGGREGATOR = "aggregator"
    LEARNER = "learner"


class Status(CustomEnum):
    FAILED = "failed"
    SUCCESS = "success"


@dataclasses.dataclass
class Topic:
    target: Target = Target.FLOPS_MANAGER
    subject: Subject
    status: Status

    def __str__(self) -> str:
        return f"{self.target}/{self.subject}/{self.status}"


class SupportedTopic(CustomEnum):
    PROJECT_OBSERVER_FAILED = str(Topic(subject=Subject.PROJECT_OBSERVER, status=Status.FAILED))

    FL_ACTORS_IMAGE_BUILDER_SUCCESS = str(
        Topic(subject=Subject.FL_ACTORS_IMAGE_BUILDER, status=Status.SUCCESS)
    )
    FL_ACTORS_IMAGE_BUILDER_FAILED = str(
        Topic(subject=Subject.FL_ACTORS_IMAGE_BUILDER, status=Status.FAILED)
    )

    TRAINED_MODEL_IMAGE_BUILDER_SUCCESS = str(
        Topic(subject=Subject.TRAINED_MODEL_IMAGE_BUILDER, status=Status.SUCCESS)
    )
    TRAINED_MODEL_IMAGE_BUILDER_FAILED = str(
        Topic(subject=Subject.TRAINED_MODEL_IMAGE_BUILDER, status=Status.FAILED)
    )

    AGGREGATOR_SUCCESS = str(Topic(subject=Subject.AGGREGATOR, status=Status.SUCCESS))
    AGGREGATOR_FAILED = str(Topic(subject=Subject.AGGREGATOR, status=Status.FAILED))

    LEARNER_FAILED = str(Topic(subject=Subject.LEARNER, status=Status.FAILED))
