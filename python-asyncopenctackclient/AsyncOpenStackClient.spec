# Created by pyp2rpm-3.3.5
%global pypi_name AsyncOpenStackClient

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Basic OpenStack async client library using asyncio

License:        None
URL:            https://github.com/DreamLab/AsyncOpenStackClient
Source0:        %{pypi_source}
BuildArch:      noarch

### Patches ###
Patch0001:  0001-Unpin-requirements.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp) >= 3
BuildRequires:  python3dist(python-dateutil) >= 2.8
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(simple-rest-client) == 0.5.4
BuildRequires:  python3dist(simplejson) >= 3.16

%description
The AsyncOpenStackClient is a asynchronous rest wrapper for the OpenStack API.
It provides a nice abstraction for authentication.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiohttp) >= 3
Requires:       python3dist(python-dateutil) >= 2.8
Requires:       python3dist(simple-rest-client) == 0.5.4
Requires:       python3dist(simplejson) >= 3.16
%description -n python3-%{pypi_name}
The AsyncOpenStackClient is a asynchronous rest wrapper for the OpenStack API.
It provides a nice abstraction for authentication.

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
%{python3_sitelib}/asyncopenstackclient
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 03 2023 Petr Vobornik <pvoborni@redhat.com> - 0.9.0-1
- Update to version 0.9.0

* Wed Feb 03 2021 Armando Neto <abiagion@redhat.com> - 0.8.1-1
- Initial package.
