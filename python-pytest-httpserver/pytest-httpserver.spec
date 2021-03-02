# Created by pyp2rpm-3.3.5
%global pypi_name pytest-httpserver

Name:           python-%{pypi_name}
Version:        0.3.6
Release:        1%{?dist}
Summary:        pytest-httpserver is a httpserver for pytest

License:        MIT
URL:            https://www.github.com/csernazs/pytest-httpserver
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pytest_httpserver-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-autopep8
BuildRequires:  python3-coverage
BuildRequires:  python3-coverage
BuildRequires:  python3-flake8
BuildRequires:  python3-ipdb
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-reno
BuildRequires:  python3-requests
BuildRequires:  python3-requests
BuildRequires:  python3-requests
BuildRequires:  python3-rope
BuildRequires:  python3-setuptools
# BuildRequires:  python3-sphinx
# BuildRequires:  python3-sphinx-rtd-theme
BuildRequires:  python3-typing
BuildRequires:  python3-werkzeug
BuildRequires:  python3-wheel

%description
This library is designed to help to test http clients without contacting the
real http server. In other words, it is a fake http server which is accessible
via localhost can be started with the pre-defined expected http requests and
their responses.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-coverage
Requires:       python3-pytest
Requires:       python3-pytest-cov
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       python3-werkzeug
%description -n python3-%{pypi_name}
This library is designed to help to test http clients without contacting the
real http server. In other words, it is a fake http server which is accessible
via localhost can be started with the pre-defined expected http requests and
their responses.

%package -n python-%{pypi_name}-doc
Summary:        pytest-httpserver documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-httpserver

%prep
%autosetup -n pytest_httpserver-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_httpserver
%{python3_sitelib}/pytest_httpserver-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 29 2021 Armando Neto <abiagion@redhat.com> - 0.3.6-1
- Initial package.
