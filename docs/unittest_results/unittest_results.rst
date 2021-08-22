.. role:: passed
.. role:: failed
.. role:: notrun
.. role:: notimplemented
.. role:: tags

Unit test results
=================

{% for testsuite in unittests %}

=============== =====
Test attribute  value
=============== =====
Number of tests {{ testsuite.attrib['tests'] }}
Failing tests   {{ testsuite.attrib['failures'] }}
Errors          {{ testsuite.attrib['errors'] }}
Skipped tests   {{ testsuite.attrib['skipped'] }}
=============== =====

{% set state = namespace(last_file = None) %}

{% for testcase in testsuite %}

{% set test_file = testcase.attrib['classname'] %}

{% if test_file != state.last_file %}
{{ test_file }}
{{ '-' * test_file|length }}
{% set state.last_file = test_file %}

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Test
      - Result
{% endif %}

    * - {{ testcase.attrib['name'] }}
      - {% if hassubelement(testcase, 'failure') %}:failed:`fail`{% else %}:passed:`pass`{% endif %}

{% endfor %}
{% endfor %}