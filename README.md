## UPDATE

- with the help of stack overflow turns out the issue is in beam 2.18.0

## Setup

- Define `PROJECT` and `STAGING_BUCKET` in both `stage_template_python2.sh` and `stage_template_python3.sh`
- install python requirements for `python2` and `python3`

## Reproduce Issue

- update requirements.txt to `apache-beam[gcp]==2.18.0` and run `pip3 install -r requirements`
- running `stage_template_python3.sh` fails to stage the template
- update requirements.txt to `apache-beam[gcp]<2.18.0` and run `pip3 install -r requirements`
- running `stage_template_python3.sh` sucesfully stages the template


```
apache_beam.error.RuntimeValueProviderError: RuntimeValueProvider(option: input, type: str, default_value: 'gs://dataflow-samples/shakespeare/kinglear.txt') not accessible
```

```
Traceback (most recent call last):
  File "run_pipeline.py", line 44, in <module>
    main()
  File "run_pipeline.py", line 41, in main
    lines = p | 'read' >> ReadFromText(wordcount_options.input)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/transforms/ptransform.py", line 906, in __ror__
    return self.transform.__ror__(pvalueish, self.label)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/transforms/ptransform.py", line 515, in __ror__
    result = p.apply(self, pvalueish, label)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/pipeline.py", line 490, in apply
    return self.apply(transform, pvalueish)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/pipeline.py", line 525, in apply
    pvalueish_result = self.runner.apply(transform, pvalueish, self._options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/runner.py", line 183, in apply
    return m(transform, input, options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/runner.py", line 189, in apply_PTransform
    return transform.expand(input)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/io/textio.py", line 542, in expand
    return pvalue.pipeline | Read(self._source)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/transforms/ptransform.py", line 515, in __ror__
    result = p.apply(self, pvalueish, label)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/pipeline.py", line 525, in apply
    pvalueish_result = self.runner.apply(transform, pvalueish, self._options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/runner.py", line 183, in apply
    return m(transform, input, options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/dataflow/dataflow_runner.py", line 1020, in apply_Read
    return self.apply_PTransform(transform, pbegin, options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/runner.py", line 189, in apply_PTransform
    return transform.expand(input)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/io/iobase.py", line 863, in expand
    return pbegin | _SDFBoundedSourceWrapper(self.source)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/pvalue.py", line 113, in __or__
    return self.pipeline.apply(ptransform, self)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/pipeline.py", line 525, in apply
    pvalueish_result = self.runner.apply(transform, pvalueish, self._options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/runner.py", line 183, in apply
    return m(transform, input, options)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/runner.py", line 189, in apply_PTransform
    return transform.expand(input)
  File "/usr/local/lib/python3.7/site-packages/apache_beam/io/iobase.py", line 1543, in expand
    | core.ParDo(self._create_sdf_bounded_source_dofn()))
  File "/usr/local/lib/python3.7/site-packages/apache_beam/io/iobase.py", line 1517, in _create_sdf_bounded_source_dofn
    estimated_size = source.estimate_size()
  File "/usr/local/lib/python3.7/site-packages/apache_beam/options/value_provider.py", line 136, in _f
    raise error.RuntimeValueProviderError('%s not accessible' % obj)
apache_beam.error.RuntimeValueProviderError: RuntimeValueProvider(option: input, type: str, default_value: 'gs://dataflow-samples/shakespeare/kinglear.txt') not accessible
```
