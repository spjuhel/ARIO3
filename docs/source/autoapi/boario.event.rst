================
``boario.event``
================

.. automodule:: boario.event

   .. contents::
      :local:

.. currentmodule:: boario.event


Classes
=======

- :py:class:`Event`:
  Undocumented.

- :py:class:`EventKapitalDestroyed`:
  Undocumented.

- :py:class:`EventArbitraryProd`:
  Undocumented.

- :py:class:`EventKapitalRecover`:
  Undocumented.

- :py:class:`EventKapitalRebuild`:
  Undocumented.


.. autoclass:: Event
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: Event
      :parts: 1
      
   .. rubric:: Attributes and Methods

.. autoclass:: EventKapitalDestroyed
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: EventKapitalDestroyed
      :parts: 1
      
   .. rubric:: Attributes and Methods

.. autoclass:: EventArbitraryProd
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: EventArbitraryProd
      :parts: 1
      
   .. rubric:: Attributes and Methods

.. autoclass:: EventKapitalRecover
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: EventKapitalRecover
      :parts: 1
      
   .. rubric:: Attributes and Methods

.. autoclass:: EventKapitalRebuild
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: EventKapitalRebuild
      :parts: 1
      
   .. rubric:: Attributes and Methods


Variables
=========

- :py:data:`Impact`
- :py:data:`IndustriesList`
- :py:data:`SectorsList`
- :py:data:`RegionsList`

.. autodata:: Impact
   :annotation:

   .. code-block:: text

      typing.Union[int, float, list, dict, numpy.ndarray, pandas.core.frame.DataFrame, pandas.core.series.Series]

.. autodata:: IndustriesList
   :annotation:

   .. code-block:: text

      typing.Union[typing.List[typing.Tuple[str, str]], pandas.core.indexes.multi.MultiIndex, numpy.ndarray]

.. autodata:: SectorsList
   :annotation:

   .. code-block:: text

      typing.Union[typing.List[str], pandas.core.indexes.base.Index, numpy.ndarray]

.. autodata:: RegionsList
   :annotation:

   .. code-block:: text

      typing.Union[typing.List[str], pandas.core.indexes.base.Index, numpy.ndarray]
