# Created by pyp2rpm-3.3.5
%global pypi_name simple-rest-client

Name:           python-%{pypi_name}
Version:        0.5.4
Release:        1%{?dist}
Summary:        Simple REST client for python 3.5+

License:        None
URL:            https://github.com/allisson/python-simple-rest-client
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3dist(aiohttp) >= 2.2
BuildRequires:  python3dist(json-encoder) >= 0.4.4
BuildRequires:  python3dist(python-status) >= 1.0.1
BuildRequires:  python3dist(requests) >= 2.13
BuildRequires:  python3dist(setuptools)

%description
Simple REST client for python 3.5+

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiohttp) >= 2.2
Requires:       python3dist(json-encoder) >= 0.4.4
Requires:       python3dist(python-status) >= 1.0.1
Requires:       python3dist(requests) >= 2.13
%description -n python3-%{pypi_name}
Simple REST client for python 3.5+

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
* Mon Mar 15 2021 Armando Neto <abiagion@redhat.com> - 0.5.4-1
- Initial package.
