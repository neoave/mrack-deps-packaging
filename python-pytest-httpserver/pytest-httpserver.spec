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
BuildRequires:  python3dist(autopep8)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(ipdb)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(reno)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rope)
BuildRequires:  python3dist(setuptools)
#BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(typing)
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(sphinx)

%description
This library is designed to help to test http clients without contacting the
real http server. In other words, it is a fake http server which is accessible
via localhost can be started with the pre-defined expected http requests and
their responses.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coverage)
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(requests)
Requires:       python3dist(setuptools)
#Requires:       python3dist(typing)
Requires:       python3dist(werkzeug)
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
