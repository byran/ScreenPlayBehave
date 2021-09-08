from behave.model import Feature, Scenario, Step
from behave.formatter.base import Formatter
from typing import List
from itertools import chain
from screenplay.log import Log
import time


class CollectedStep:
    def __init__(self, name: str, step_type: str, text: List[str] = [],
                 error_message: List[str] = None, status: str = 'not run'):
        self.name = name
        self.step_type = step_type
        self.text: List[str] = text
        self.error_message = error_message
        self.status = status

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class CollectedScenario:
    def __init__(self, name: str, tags: List[str], status: str = 'not run',
                 steps: List[CollectedStep] = None):
        self.name = name
        self.tags: List[str] = tags
        self.status = status
        self.steps: List[CollectedStep] = [] if (steps is None) else steps

    @classmethod
    def from_json(cls, data):
        steps = list(map(CollectedStep.from_json, data['steps']))
        data.pop('steps', None)
        return cls(steps=steps, **data)


class CollectedRule:
    def __init__(self, name: str, description: List[str],
                 tags: List[str], scenarios: List[CollectedScenario] = None):
        self.name = name
        self.description: List[str] = description
        self.tags: List[str] = tags
        self.scenarios: List[CollectedScenario] = [] if (scenarios is None) else scenarios

    @classmethod
    def from_json(cls, data):
        scenarios = list(map(CollectedScenario.from_json, data['scenarios']))
        data.pop('scenarios', None)
        return cls(scenarios=scenarios, **data)


class CollectedFeature:
    def __init__(self, file_name: str, name: str, description: List[str],
                 tags: List[str], start_time: float = time.time(),
                 run_time: float = 0, scenarios: List[CollectedScenario] = None,
                 rules: List[CollectedRule] = None):
        self.file_name = file_name
        self.name = name
        self.description: List[str] = description
        self.tags: List[str] = tags
        self.start_time = start_time
        self.run_time = run_time
        self.scenarios: List[CollectedScenario] = [] if (scenarios is None) else scenarios
        self.rules: List[CollectedRule] = [] if (rules is None) else rules

    def finished(self):
        self.run_time = time.time() - self.start_time

    @classmethod
    def from_json(cls, data):
        scenarios = list(map(CollectedScenario.from_json, data['scenarios']))
        data.pop('scenarios', None)
        rules = list(map(CollectedRule.from_json, data['rules']))
        data.pop('rules', None)
        return cls(scenarios=scenarios, rules=rules, **data)


class CollectingFormatter(Formatter):
    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)

        self.currentFeature: CollectedFeature = None
        self.currentRule: CollectedRule = None
        self.currentScenario: CollectedScenario = None
        self.currentStep: CollectedStep = None

        self.stepsToProcess: List[CollectedStep] = []
        self.currentStep_text: List[str] = []

        Log.write_line = self.write_function()

    def write_function(self):
        def formatter_write_line(*values, sep=''):
            line = sep.join(map(str, chain.from_iterable(values)))
            print(line)
            self.currentStep_text.append(line)
        return formatter_write_line

    def feature(self, feature: Feature):
        self.currentFeature = CollectedFeature(feature.filename, feature.name, feature.description, feature.tags)

    def rule(self, rule):
        self.currentRule = CollectedRule(rule.name, rule.description, rule.tags)
        self.currentFeature.rules.append(self.currentRule)

    def background(self, background):
        pass

    def scenario(self, scenario: Scenario):
        self.currentScenario = CollectedScenario(scenario.name, scenario.tags)
        if self.currentRule is None:
            self.currentFeature.scenarios.append(self.currentScenario)
        else:
            self.currentRule.scenarios.append(self.currentScenario)

        self.stepsToProcess = []

    def step(self, step: Step):
        stepToStore = CollectedStep(step.name, step.keyword)
        self.currentScenario.steps.append(stepToStore)

        self.stepsToProcess.append(stepToStore)

    def match(self, match):
        self.currentStep = self.stepsToProcess.pop(0)
        self.currentStep_text = []

    def result(self, step_result):
        self.currentStep.status = step_result.status.name
        self.currentStep.text = self.currentStep_text
        self.currentStep.error_message = step_result.error_message

        self.currentScenario.status = step_result.status.name

    def eof(self):
        self.currentFeature.finished()
