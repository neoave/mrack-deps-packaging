# Created by pyp2rpm-3.3.5
%global pypi_name simple-rest-client

Name:           python-%{pypi_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        Simple REST client for python 3.6+

License:        None
URL:            https://github.com/allisson/python-simple-rest-client
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-coveralls
BuildRequires:  python3-httpx
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-httpserver
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-slugify
BuildRequires:  python3-status
BuildRequires:  python3-setuptools

%description
Simple REST client for python 3.6+.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-httpx
Requires:       python3-slugify
Requires:       python3-status
%description -n python3-%{pypi_name}
Simple REST client for python 3.6+.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/simple_rest_client
%{python3_sitelib}/simple_rest_client-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jan 28 2021 Armando Neto <abiagion@redhat.com> - 1.0.8-1
- Initial package.
