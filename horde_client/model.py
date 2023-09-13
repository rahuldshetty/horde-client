from enum import Enum
from pydantic import BaseModel
from typing import List

class ModelType(str, Enum):
    text = 'text'
    image = 'image'

class Model(BaseModel):
    name: str
    count: int
    eta: int
    jobs: float
    performance: float
    queued: float
    type: ModelType

    def __str__(self) -> str:
        return "Model({name}, perf={perf})".format(
            name = self.name,
            perf = self.performance
        )

class TextGenParams(BaseModel):
    frmtadsnsp: bool = False
    frmtrmblln: bool = False
    frmtrmspch: bool = False
    frmttriminc: bool = False
    max_context_length: int = 1024
    max_length: int = 100
    n: int = 1
    rep_pen: float = 1.1
    rep_pen_range: int = 320
    rep_pen_slope: float = 0.7
    temperature: float = 0.7
    sampler_order: List[int | None] =  [6, 0, 1, 3, 4, 2, 5]
    tfs: int = 1
    top_a: int = 0
    top_k: int = 0
    top_p: float = 0.92
    typical: int = 1


class TextGenRequest(BaseModel):
    models: List[str]
    params: TextGenParams
    prompt: str
    use_default_badwordsids: bool = True
    workers: List[str] = []

class Job(BaseModel):
    id: str
    kudos: int

class JobGenerationOutputState(str, Enum):
    ok = "ok"
    censored = "censored"

class JobGenerationOutput(BaseModel):
    worker_id: str
    worker_name: str
    text: str
    state: JobGenerationOutputState
    seed: int
    model: str

class JobResponse(BaseModel):
    done: bool
    faulted: bool
    generations: List[JobGenerationOutput]
    is_possible: bool
    kudos: int
    processing: int
    queue_position: int
    restarted: int
    wait_time: int
    waiting: int

    def __str__(self) -> str:
        return "Output(done={done},responses=[{responses}])".format(
            done = str(self.done),
            responses = str(len(self.generations))
        )

