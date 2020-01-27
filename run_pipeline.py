# from __future__ import absolute_import
# from __future__ import print_function
# from __future__ import division

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions

from apache_beam.io import ReadFromText

class WordcountOptions(PipelineOptions):
  @classmethod
  def _add_argparse_args(cls, parser):
    # Use add_value_provider_argument for arguments to be templatable
    # Use add_argument as usual for non-templatable arguments
    parser.add_value_provider_argument(
      '--input',
      default='gs://dataflow-samples/shakespeare/kinglear.txt',
      help='Path of the file to read from',
      dest="input")
  
def main(argv=None):
  # options = PipelineOptions(flags=argv)
  # review_processing_options = options.view_as(TemplateReviewProcessingOptions)

  # #installing packages used in process
  # setup_options = options.view_as(SetupOptions)
  # setup_options.save_main_session = True   

  # pipeline.run(options, review_processing_options)

  options = PipelineOptions(flags=argv)
  setup_options = options.view_as(SetupOptions)
  # setup_options.setup_file = './setup.py'
  # setup_options.save_main_session = False 

  wordcount_options = options.view_as(WordcountOptions)

  with beam.Pipeline(options=setup_options) as p:
    lines = p | 'read' >> ReadFromText(wordcount_options.input)

if __name__ == '__main__':
  main()