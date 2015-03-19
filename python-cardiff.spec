Name:           python-cardiff
Version:        0.9.0
Release:        1%{?dist}
Summary:        Analyze eDeploy AHC Results

License:        ASL 2.0
URL:            https://github.com/rdo-management/cardiff
Source0:        https://github.com/rdo-management/cardiff/archive/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  python-pbr
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       numpy
Requires:       python-pandas

BuildArch:      noarch

%description
A tool/library for analyzing eDeploy AHC results


%prep
%setup -q -n cardiff-%{version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt


%build
# strong-arm the ironically named PBR into being reasonable
export PBR_VERSION="%{version}"
%{__python} setup.py build


%install
# strong-arm the ironically named PBR into being reasonable
export PBR_VERSION="%{version}"
%{__python} setup.py install --skip-build --root=%{buildroot}


%files
%{_bindir}/cardiff
%{python_sitelib}/cardiff
%{python_sitelib}/*.egg-info


%changelog
* Thu Mar 19 2015 Solly Ross <sross@redhat.com> - 0.9.0-1
- Initial Packaging
