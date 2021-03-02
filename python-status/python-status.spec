# Created by pyp2rpm-3.3.5
%global pypi_name python-status
%global srcname status

Name:           python-%{srcname}
Version:        1.0.1
Release:        1%{?dist}
Summary:        HTTP Status for Humans

License:        BSD
URL:            https://github.com/avinassh/status/
Source0:        %{pypi_source python-status}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
status is a very simple python library which provides human understandable HTTP
status codes and improves readability of your code. You don't have to use those
ugly HTTP status numbers, but use easily understandable status names.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
status is a very simple python library which provides human understandable HTTP
status codes and improves readability of your code. You don't have to use those
ugly HTTP status numbers, but use easily understandable status names.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/status.py
%{python3_sitelib}/python_status-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 29 2021 Armando Neto <abiagion@redhat.com> - 1.0.1-1
- Initial package.
