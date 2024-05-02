###############################################################################
# Imports
###############################################################################

###############################################################################
# from articles.tests
###############################################################################

# pytest tests/tests.py::ClientArticleCreationTestCase
from articles.tests.tests import ArticleCreationTestCase as ClientArticleCreationTestCase

# pytest tests/tests.py::ClientArticleDeletionTestCase
from articles.tests.tests import ArticleDeletionTestCase as ClientArticleDeletionTestCase

# pytest tests/tests.py::ClientArticleRetrieveTestCase
from articles.tests.tests import ArticleRetrieveTestCase as ClientArticleRetrieveTestCase

# pytest tests/tests.py::ClientUpdateTestCase
from articles.tests.tests import ArticleUpdateTestCase as ClientArticleUpdateTestCase

###############################################################################
# from projects.tests
###############################################################################

# pytest tests/tests.py::ClientCreateProjectTestCase
from projects.tests.tests import CreateProjectTestCase as ClientCreateProjectTestCase

# pytest tests/tests.py::ClientUpdateProjectTestCase
from projects.tests.tests import UpdateProjectTestCase as ClientUpdateProjectTestCase

# pytest tests/tests.py::ClientDeleteProjectTestCase
from projects.tests.tests import DeleteProjectTestCase as ClientDeleteProjectTestCase

# pytest tests/tests.py::ClientRetrieveProjectTestCase
from projects.tests.tests import RetrieveProjectTestCase as ClientRetrieveProjectTestCase




